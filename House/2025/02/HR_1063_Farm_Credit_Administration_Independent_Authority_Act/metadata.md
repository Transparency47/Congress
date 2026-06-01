# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1063?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1063
- Title: Farm Credit Administration Independent Authority Act
- Congress: 119
- Bill type: HR
- Bill number: 1063
- Origin chamber: House
- Introduced date: 2025-02-06
- Update date: 2026-02-27T09:06:49Z
- Update date including text: 2026-02-27T09:06:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-06 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-07 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.
- Latest action: 2025-02-06: Introduced in House

## Actions

- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-06 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-07 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1063",
    "number": "1063",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000475",
        "district": "1",
        "firstName": "Brad",
        "fullName": "Rep. Finstad, Brad [R-MN-1]",
        "lastName": "Finstad",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "Farm Credit Administration Independent Authority Act",
    "type": "HR",
    "updateDate": "2026-02-27T09:06:49Z",
    "updateDateIncludingText": "2026-02-27T09:06:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-07",
      "committees": {
        "item": {
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-02-06T15:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-07T17:20:28Z",
              "name": "Referred to"
            }
          },
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-06T15:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "IL"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "IN"
    },
    {
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "MN"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "MI"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "TX"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "MN"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "MI"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "MI"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "CA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "VA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "PA"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "KY"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "KS"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1063ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1063\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 6, 2025 Mr. Finstad (for himself, Mr. Panetta , Mrs. Miller of Illinois , Mr. Baird , Mrs. Fischbach , and Mr. Moolenaar ) introduced the following bill; which was referred to the Committee on Agriculture , and in addition to the Committee on Financial Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo affirm that the Farm Credit Administration is the sole and independent regulator of the Farm Credit System.\n#### 1. Short title\nThis Act may be cited as the Farm Credit Administration Independent Authority Act .\n#### 2. Farmer loan data collection\n##### (a) In general\nThe Farm Credit Act of 1971 ( 12 U.S.C. 2001 et seq. ) is amended by inserting after section 4.19 the following:\n4.20. Small farmer loan data collection (a) Purpose The purpose of this section is to affirm that the Farm Credit Administration is the sole and independent regulator of the Farm Credit System. (b) Definition In this section, the term small farmer means a small farmer, rancher, or producer or harvester of aquatic products as defined pursuant to section 4.19. (c) Collection of demographic data by Farm Credit System lenders Notwithstanding any other provision of law, Farm Credit System institutions, pursuant to regulations promulgated by the Farm Credit Administration, shall\u2014 (1) request that loan applicants and borrowers that are small farmers disclose information identifying their race, sex, and ethnicity; (2) collect and maintain the information resulting from the requests; and (3) report to the Farm Credit Administration on an annual basis the information collected pursuant to the requests. (d) Directions to the Farm Credit Administration The Farm Credit Administration\u2014 (1) shall collect the information gathered by Farm Credit System institutions under this section and make the information available to the public on an annual basis; and (2) shall not require, in prescribing regulations to implement this section, that any Farm Credit System institution contradict the wishes of a customer who does not wish to voluntarily report race, sex, or ethnicity by requiring the Farm Credit System institution to report the race, sex, or ethnicity of the customer based on visual observation, surname, or any other method. (e) Protection of personally identifiable information In reporting the information collected under this section, the Farm Credit Administration shall not include any information that would reveal the identify of any loan applicant or borrower. (f) Effective date This section shall apply only to applications received and loans made 1 year or more after the date of the enactment of this section. .\n#### 3. Conforming amendment\nSection 704B(h)(1) of the Equal Credit Opportunity Act ( 15 U.S.C. 1691c\u20132(h)(1) ) is amended by inserting , other than any entity that is supervised by the Farm Credit Administration before the period at the end.\n#### 4. Cessation of compliance\nIf financial institutions subject to subpart B of part 1002 of title 12, Code of Federal Regulations, are not required to comply with the rule promulgated pursuant to that subpart, whether because a court invalidates the rule or the rule is otherwise repealed, the Farm Credit System institutions shall not be required to comply with any regulation promulgated pursuant to the amendments made by this Act.",
      "versionDate": "2025-02-06",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Agriculture and Food",
        "updateDate": "2025-03-20T18:32:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1063",
          "measure-number": "1063",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-06",
          "originChamber": "HOUSE",
          "update-date": "2025-03-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1063v00",
            "update-date": "2025-03-26"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Farm Credit Administration Independent Authority Act</strong></p><p>This bill specifies that the Farm Credit Administration (FCA) is the sole regulator of the Farm Credit System (FCS) and establishes reporting requirements for FCS institutions (i.e., lenders).</p><p>Specifically, the bill states that the FCA is the sole and independent regulator of the FCS and exempts entities that are supervised by the FCA from the Equal Credit Opportunity Act (ECOA).</p><p>As background, the bill addresses a rule issued by the Consumer Financial Protection Bureau (CFPB) that implements provisions of the ECOA by requiring covered financial institutions, including FCS institutions, to collect and report to the CFPB data on credit applications for small businesses, including the principal owner's race, sex, and ethnicity. This 2023 rule has been challenged in court.</p><p>The bill also requires FCS institutions to (1) request that loan applicants and borrowers that are small farmers disclose information identifying their race, sex, and ethnicity; and (2) annually report the collected information to the FCA.\u00a0The FCA must make the collected information available to the public on annual basis.\u00a0If an FCS institution customer does not voluntarily report the requested information, the FCA may not require the institution to use other means to deduce the information.</p><p>In addition, the bill specifies that\u00a0FCS institutions shall not be required to comply with the bill's requirements if financial institutions are not required to comply with the CFPB rule due to a court invalidating the rule or a repeal of the rule.</p>"
        },
        "title": "Farm Credit Administration Independent Authority Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1063.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Farm Credit Administration Independent Authority Act</strong></p><p>This bill specifies that the Farm Credit Administration (FCA) is the sole regulator of the Farm Credit System (FCS) and establishes reporting requirements for FCS institutions (i.e., lenders).</p><p>Specifically, the bill states that the FCA is the sole and independent regulator of the FCS and exempts entities that are supervised by the FCA from the Equal Credit Opportunity Act (ECOA).</p><p>As background, the bill addresses a rule issued by the Consumer Financial Protection Bureau (CFPB) that implements provisions of the ECOA by requiring covered financial institutions, including FCS institutions, to collect and report to the CFPB data on credit applications for small businesses, including the principal owner's race, sex, and ethnicity. This 2023 rule has been challenged in court.</p><p>The bill also requires FCS institutions to (1) request that loan applicants and borrowers that are small farmers disclose information identifying their race, sex, and ethnicity; and (2) annually report the collected information to the FCA.\u00a0The FCA must make the collected information available to the public on annual basis.\u00a0If an FCS institution customer does not voluntarily report the requested information, the FCA may not require the institution to use other means to deduce the information.</p><p>In addition, the bill specifies that\u00a0FCS institutions shall not be required to comply with the bill's requirements if financial institutions are not required to comply with the CFPB rule due to a court invalidating the rule or a repeal of the rule.</p>",
      "updateDate": "2025-03-26",
      "versionCode": "id119hr1063"
    },
    "title": "Farm Credit Administration Independent Authority Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Farm Credit Administration Independent Authority Act</strong></p><p>This bill specifies that the Farm Credit Administration (FCA) is the sole regulator of the Farm Credit System (FCS) and establishes reporting requirements for FCS institutions (i.e., lenders).</p><p>Specifically, the bill states that the FCA is the sole and independent regulator of the FCS and exempts entities that are supervised by the FCA from the Equal Credit Opportunity Act (ECOA).</p><p>As background, the bill addresses a rule issued by the Consumer Financial Protection Bureau (CFPB) that implements provisions of the ECOA by requiring covered financial institutions, including FCS institutions, to collect and report to the CFPB data on credit applications for small businesses, including the principal owner's race, sex, and ethnicity. This 2023 rule has been challenged in court.</p><p>The bill also requires FCS institutions to (1) request that loan applicants and borrowers that are small farmers disclose information identifying their race, sex, and ethnicity; and (2) annually report the collected information to the FCA.\u00a0The FCA must make the collected information available to the public on annual basis.\u00a0If an FCS institution customer does not voluntarily report the requested information, the FCA may not require the institution to use other means to deduce the information.</p><p>In addition, the bill specifies that\u00a0FCS institutions shall not be required to comply with the bill's requirements if financial institutions are not required to comply with the CFPB rule due to a court invalidating the rule or a repeal of the rule.</p>",
      "updateDate": "2025-03-26",
      "versionCode": "id119hr1063"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1063ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Farm Credit Administration Independent Authority Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:08Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Farm Credit Administration Independent Authority Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T03:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To affirm that the Farm Credit Administration is the sole and independent regulator of the Farm Credit System.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T03:03:37Z"
    }
  ]
}
```
