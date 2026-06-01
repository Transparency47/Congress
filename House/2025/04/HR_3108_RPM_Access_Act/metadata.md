# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3108?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3108
- Title: RPM Access Act
- Congress: 119
- Bill type: HR
- Bill number: 3108
- Origin chamber: House
- Introduced date: 2025-04-30
- Update date: 2026-05-13T08:06:50Z
- Update date including text: 2026-05-13T08:06:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-30: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-30 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-30: Introduced in House

## Actions

- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-30 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3108",
    "number": "3108",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000392",
        "district": "8",
        "firstName": "David",
        "fullName": "Rep. Kustoff, David [R-TN-8]",
        "lastName": "Kustoff",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "RPM Access Act",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:50Z",
    "updateDateIncludingText": "2026-05-13T08:06:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T14:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-30T14:03:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "OH"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "NC"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "WI"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "WV"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "VA"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "NE"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "FL"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "MI"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3108ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3108\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2025 Mr. Kustoff (for himself, Mr. Balderson , Mr. Davis of North Carolina , and Mr. Pocan ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act with respect to payment for remote patient monitoring under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Rural Patient Monitoring Access Act or the RPM Access Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nRemote patient monitoring (in this section referred to as RPM ) supports highly coordinated care, improves patient outcomes, and can lower costs to the Medicare program.\n**(2)**\nThree out of five federally designated health professional shortage areas are in rural regions, and rural residents generally must travel farther than urban counterparts to access health care services.\n**(3)**\nMedicare reimbursement for RPM is lowest in States where the prevalence of heart failure, hypertension, and diabetes are well above the national average.\n**(4)**\nThe practice expenses and malpractice expenses incurred in the delivery of RPM are not lower in rural areas and do not widely vary by State.\n#### 3. Floor for practice expense and malpractice geographic indices for remote patient monitoring\nSection 1848(e)(1) of the Social Security Act ( 42 U.S.C. 1395w\u20134(e)(1) ) is amended by adding at the end the following new subparagraph:\n(J) Floor for practice expense and malpractice geographic indices for remote patient monitoring For purposes of payment for remote patient monitoring furnished on or after January 1, 2026, after calculating the practice expense and malpractice geographic indices in clauses (i) and (ii) of subparagraph (A) and in subparagraph (B), the Secretary shall increase any such index to 1.00 if such index would otherwise be less than 1.00. The preceding sentence shall not be applied in a budget neutral manner. .\n#### 4. Ensuring high-quality remote patient monitoring under Medicare\n##### (a) In general\nSection 1834 of the Social Security Act ( 42 U.S.C. 1395m ) is amended by adding at the end the following new subsection:\n(aa) Payment for remote patient monitoring In the case of remote patient monitoring furnished on or after January 1, 2026, no payment may be made under this part for such monitoring furnished by a provider of services or supplier unless\u2014 (1) a physician, nurse practitioner, clinical nurse specialist, or physician assistant is available in real time to respond to any physiologic anomaly detected through such monitoring; (2) such monitoring is furnished through a system that can transmit physiologic data obtained through such monitoring in a format that is compatible with electronic health records, as needed; and (3) the provider or supplier collects and reports such data as the Secretary may require in order to facilitate the evaluation of cost savings to the program under this title that are generated by the use of remote patient monitoring, except that the Secretary may exempt a provider or supplier under this paragraph if the Secretary determines that such collection and reporting of data would result in unreasonable hardship upon such provider or supplier. .\n##### (b) Report\n**(1) In general**\nNot later than 5 years after the date of the enactment of this section, the Secretary of Health and Human Services shall submit to Congress a report that includes the following information, with respect to the 4-year period beginning January 1, 2026:\n**(A)**\nAn analysis of the estimated savings to the Medicare program resulting from earlier interventions and fewer days of hospitalization among Medicare beneficiaries furnished remote patient monitoring (as such term is used for purposes of title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. )) during such period.\n**(B)**\nAn analysis of the estimated savings to the Medicare program resulting from increased adherence to prescription medications among Medicare beneficiaries furnished remote patient monitoring during such period.\n**(C)**\nAn analysis of practice expenses as defined in section 1848(j) of the Social Security Act ( 42 U.S.C. 1395w\u20134(j) ) related to the furnishing of remote patient monitoring during such period, including expenses related to cellular connectivity and other technology platform maintenance.\n**(2) Definitions**\nIn this subsection:\n**(A) Medicare beneficiary**\nThe term Medicare beneficiary means an individual entitled to benefits under part A of title XVIII of the Social Security Act ( 42 U.S.C. 1395c et seq. ) or enrolled under part B of such title ( 42 U.S.C. 1395j et seq. )\n**(B) Medicare program**\nThe term Medicare program means the Medicare program under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ).",
      "versionDate": "2025-04-30",
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
        "name": "Health",
        "updateDate": "2025-05-21T10:56:58Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-30",
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
          "measure-id": "id119hr3108",
          "measure-number": "3108",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-30",
          "originChamber": "HOUSE",
          "update-date": "2025-05-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3108v00",
            "update-date": "2025-05-21"
          },
          "action-date": "2025-04-30",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Rural Patient Monitoring Access Act or the RPM Access Act</strong></p><p>This bill conditions Medicare payment for remote patient monitoring services on certain requirements.</p><p>Specifically, the bill conditions payment on (1) the ability of certain health care practitioners to be available in real time to respond to any detected anomalies; (2) the use of a system that can transmit relevant data in a format that is compatible with electronic health records, as needed; and (3) the reporting of such data, as required by the Centers for Medicare & Medicaid Services (CMS), to evaluate any cost savings as a\u00a0result of such services.</p><p>The bill also establishes a floor for certain payment calculations with respect to such services.</p><p>The CMS must report on cost savings realized and expenses incurred from the use of such services over a four-year period.</p><p>\u00a0</p>"
        },
        "title": "RPM Access Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3108.xml",
    "summary": {
      "actionDate": "2025-04-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Rural Patient Monitoring Access Act or the RPM Access Act</strong></p><p>This bill conditions Medicare payment for remote patient monitoring services on certain requirements.</p><p>Specifically, the bill conditions payment on (1) the ability of certain health care practitioners to be available in real time to respond to any detected anomalies; (2) the use of a system that can transmit relevant data in a format that is compatible with electronic health records, as needed; and (3) the reporting of such data, as required by the Centers for Medicare & Medicaid Services (CMS), to evaluate any cost savings as a\u00a0result of such services.</p><p>The bill also establishes a floor for certain payment calculations with respect to such services.</p><p>The CMS must report on cost savings realized and expenses incurred from the use of such services over a four-year period.</p><p>\u00a0</p>",
      "updateDate": "2025-05-21",
      "versionCode": "id119hr3108"
    },
    "title": "RPM Access Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Rural Patient Monitoring Access Act or the RPM Access Act</strong></p><p>This bill conditions Medicare payment for remote patient monitoring services on certain requirements.</p><p>Specifically, the bill conditions payment on (1) the ability of certain health care practitioners to be available in real time to respond to any detected anomalies; (2) the use of a system that can transmit relevant data in a format that is compatible with electronic health records, as needed; and (3) the reporting of such data, as required by the Centers for Medicare & Medicaid Services (CMS), to evaluate any cost savings as a\u00a0result of such services.</p><p>The bill also establishes a floor for certain payment calculations with respect to such services.</p><p>The CMS must report on cost savings realized and expenses incurred from the use of such services over a four-year period.</p><p>\u00a0</p>",
      "updateDate": "2025-05-21",
      "versionCode": "id119hr3108"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3108ih.xml"
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
      "title": "RPM Access Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-13T05:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RPM Access Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Patient Monitoring Access Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act with respect to payment for remote patient monitoring under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:18:42Z"
    }
  ]
}
```
