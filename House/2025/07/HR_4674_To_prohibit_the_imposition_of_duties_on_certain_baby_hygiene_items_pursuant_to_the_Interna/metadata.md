# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4674?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4674
- Title: Baby Hygiene Tax Relief Act
- Congress: 119
- Bill type: HR
- Bill number: 4674
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-05-11T18:37:26Z
- Update date including text: 2026-05-11T18:37:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-23 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-23 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4674",
    "number": "4674",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "H001066",
        "district": "4",
        "firstName": "Steven",
        "fullName": "Rep. Horsford, Steven [D-NV-4]",
        "lastName": "Horsford",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Baby Hygiene Tax Relief Act",
    "type": "HR",
    "updateDate": "2026-05-11T18:37:26Z",
    "updateDateIncludingText": "2026-05-11T18:37:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:03:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-23T14:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "VA"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "True",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "AL"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "NY"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4674ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4674\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Horsford (for himself, Mr. Gomez , Mr. Subramanyam , Mr. Tran , Mr. Schneider , and Mr. Figures ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Foreign Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit the imposition of duties on certain baby hygiene items pursuant to the International Emergency Economic Powers Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Baby Hygiene Tax Relief Act .\n#### 2. Prohibition on imposition of duties on certain baby hygiene items pursuant to the International Emergency Economic Powers Act\n##### (a) In general\nNotwithstanding any other provision of law, the President\u2014\n**(1)**\nmay not impose duties on the items described in section 3 pursuant to the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ); and\n**(2)**\nshall terminate the imposition of duties on the items described in section 3 pursuant to the International Emergency Economic Powers Act that are in effect as of the date of the enactment of this Act.\n##### (b) Duties under other authorities\nAny duties imposed by the President on the items described in section 3 pursuant to any other authority that are substantially similar to the duties imposed pursuant to the International Emergency Economic Powers Act shall have no force or effect.\n#### 3. Items described\nThe items described in this section are the following:\n**(1)**\nDiapers.\n**(2)**\nDiaper liners.\n**(3)**\nDiaper cream.\n**(4)**\nDiaper bags.\n**(5)**\nChanging tables.\n**(6)**\nBaby wipes.\n**(7)**\nBaby soap.\n**(8)**\nBaby shampoo.\n**(9)**\nBaby changing tables.\n**(10)**\nBaby bathtubs.\n**(11)**\nBaby towels.",
      "versionDate": "2025-07-23",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-09-17T19:39:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-23",
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
          "measure-id": "id119hr4674",
          "measure-number": "4674",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-23",
          "originChamber": "HOUSE",
          "update-date": "2026-05-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4674v00",
            "update-date": "2026-05-11"
          },
          "action-date": "2025-07-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Baby Hygiene Tax Relief Act</strong></p><p>This bill prohibits the imposition of duties (i.e., tariffs) on specified baby hygiene items (e.g., diapers, baby wipes, and baby changing tables) pursuant to certain presidential powers.</p><p>Specifically, the bill\u00a0prohibits the President from exercising authorities under the International Emergency Economic Powers Act (IEEPA) to impose duties on specified baby hygiene items entering the United States. (IEEPA provides the President with broad authority to regulate various economic transactions following a declaration of a national emergency.)</p><p>Further, the President must terminate the duties on these items that were imposed pursuant to IEEPA and are in effect as of the date of the bill's enactment.</p><p>The bill also prohibits the President from using any other authorities to impose duties on these items that are substantially similar to the duties imposed pursuant to IEEPA.</p>"
        },
        "title": "Baby Hygiene Tax Relief Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4674.xml",
    "summary": {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Baby Hygiene Tax Relief Act</strong></p><p>This bill prohibits the imposition of duties (i.e., tariffs) on specified baby hygiene items (e.g., diapers, baby wipes, and baby changing tables) pursuant to certain presidential powers.</p><p>Specifically, the bill\u00a0prohibits the President from exercising authorities under the International Emergency Economic Powers Act (IEEPA) to impose duties on specified baby hygiene items entering the United States. (IEEPA provides the President with broad authority to regulate various economic transactions following a declaration of a national emergency.)</p><p>Further, the President must terminate the duties on these items that were imposed pursuant to IEEPA and are in effect as of the date of the bill's enactment.</p><p>The bill also prohibits the President from using any other authorities to impose duties on these items that are substantially similar to the duties imposed pursuant to IEEPA.</p>",
      "updateDate": "2026-05-11",
      "versionCode": "id119hr4674"
    },
    "title": "Baby Hygiene Tax Relief Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Baby Hygiene Tax Relief Act</strong></p><p>This bill prohibits the imposition of duties (i.e., tariffs) on specified baby hygiene items (e.g., diapers, baby wipes, and baby changing tables) pursuant to certain presidential powers.</p><p>Specifically, the bill\u00a0prohibits the President from exercising authorities under the International Emergency Economic Powers Act (IEEPA) to impose duties on specified baby hygiene items entering the United States. (IEEPA provides the President with broad authority to regulate various economic transactions following a declaration of a national emergency.)</p><p>Further, the President must terminate the duties on these items that were imposed pursuant to IEEPA and are in effect as of the date of the bill's enactment.</p><p>The bill also prohibits the President from using any other authorities to impose duties on these items that are substantially similar to the duties imposed pursuant to IEEPA.</p>",
      "updateDate": "2026-05-11",
      "versionCode": "id119hr4674"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4674ih.xml"
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
      "title": "Baby Hygiene Tax Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-07T10:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Baby Hygiene Tax Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-07T10:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the imposition of duties on certain baby hygiene items pursuant to the International Emergency Economic Powers Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-07T10:03:19Z"
    }
  ]
}
```
