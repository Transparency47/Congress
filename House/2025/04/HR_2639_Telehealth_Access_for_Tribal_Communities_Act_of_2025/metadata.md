# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2639?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2639
- Title: Telehealth Access for Tribal Communities Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2639
- Origin chamber: House
- Introduced date: 2025-04-03
- Update date: 2026-05-21T19:58:38Z
- Update date including text: 2026-05-21T19:58:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-03: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-03 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-03: Introduced in House

## Actions

- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-03 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2639",
    "number": "2639",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000273",
        "district": "3",
        "firstName": "Teresa",
        "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
        "lastName": "Leger Fernandez",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Telehealth Access for Tribal Communities Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T19:58:38Z",
    "updateDateIncludingText": "2026-05-21T19:58:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-03",
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
      "actionDate": "2025-04-03",
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
      "actionDate": "2025-04-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-03",
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
          "date": "2025-04-03T15:04:30Z",
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
          "date": "2025-04-03T15:04:25Z",
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
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "NM"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "CA"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "DC"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "AZ"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "CO"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2639ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2639\nIN THE HOUSE OF REPRESENTATIVES\nApril 3, 2025 Ms. Leger Fernandez (for herself, Ms. Stansbury , Mr. Ruiz , Mr. Obernolte , and Ms. Norton ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to make permanent certain telehealth flexibilities under the Medicare program for telehealth services furnished by Indian health programs.\n#### 1. Short title\nThis Act may be cited as the Telehealth Access for Tribal Communities Act of 2025 .\n#### 2. Making permanent certain telehealth flexibilities under the Medicare program for telehealth services furnished by Indian health programs\nSection 1834(m) of the Social Security Act ( 42 U.S.C. 1395m(m) ) is amended\u2014\n**(1)**\nin paragraph (4)(C)(iii)\u2014\n**(A)**\nby striking In the case and inserting the following:\n(I) In general In the case ; and\n**(B)**\nby adding at the end the following new subclause:\n(II) Special rule for services furnished by Indian health programs With respect to telehealth services identified in subparagraph (F)(i) as of the date of the enactment of this clause furnished on or after April 1, 2025, by an Indian health program (as defined in section 4 of the Indian Health Care Improvement Act) or by an urban Indian organization (as so defined), or by a physician or practitioner employed by or under contract with such a program or organization, to an eligible telehealth individual, the term originating site means any site in the United States at which the eligible telehealth individual is located at the time the service is furnished via a telecommunications system, including the home of an individual. ; and\n**(2)**\nin paragraph (9)\u2014\n**(A)**\nby striking In the case and inserting the following:\n(A) In general In the case ; and\n**(B)**\nby adding at the end the following new subparagraph:\n(B) Special rule for services furnished by Indian health programs The Secretary shall provide coverage and payment under this part for telehealth services identified in subparagraph (F)(i) as of the date of the enactment of this paragraph that are furnished on or after April 1, 2025, via an audio-only communications system by an Indian health program (as defined in section 4 of the Indian Health Care Improvement Act) or by an urban Indian organization (as so defined), or by a physician or practitioner employed by or under contract with such a program or organization, to an eligible telehealth individual. For purposes of the previous sentence, the term telehealth service means a telehealth service identified as of the date of the enactment of this paragraph by a HCPCS code (and any succeeding codes) for which the Secretary has not applied the requirements of paragraph (1) and the first sentence of section 410.78(a)(3) of title 42, Code of Federal Regulations, during the emergency period described in subparagraph (A). .",
      "versionDate": "2025-04-03",
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
        "updateDate": "2025-04-11T14:31:47Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-03",
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
          "measure-id": "id119hr2639",
          "measure-number": "2639",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-03",
          "originChamber": "HOUSE",
          "update-date": "2026-05-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2639v00",
            "update-date": "2026-05-21"
          },
          "action-date": "2025-04-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Telehealth Access for Tribal Communities Act of 2025</strong></p><p>This bill permanently provides for Medicare coverage of audio-only, at-home telehealth services that are furnished through the Indian Health Service.</p>"
        },
        "title": "Telehealth Access for Tribal Communities Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2639.xml",
    "summary": {
      "actionDate": "2025-04-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Telehealth Access for Tribal Communities Act of 2025</strong></p><p>This bill permanently provides for Medicare coverage of audio-only, at-home telehealth services that are furnished through the Indian Health Service.</p>",
      "updateDate": "2026-05-21",
      "versionCode": "id119hr2639"
    },
    "title": "Telehealth Access for Tribal Communities Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Telehealth Access for Tribal Communities Act of 2025</strong></p><p>This bill permanently provides for Medicare coverage of audio-only, at-home telehealth services that are furnished through the Indian Health Service.</p>",
      "updateDate": "2026-05-21",
      "versionCode": "id119hr2639"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2639ih.xml"
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
      "title": "Telehealth Access for Tribal Communities Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T10:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Telehealth Access for Tribal Communities Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T10:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to make permanent certain telehealth flexibilities under the Medicare program for telehealth services furnished by Indian health programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T10:18:19Z"
    }
  ]
}
```
