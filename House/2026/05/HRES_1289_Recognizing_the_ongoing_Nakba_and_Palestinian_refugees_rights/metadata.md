# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1289?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1289
- Title: Recognizing the ongoing Nakba and Palestinian refugees' rights.
- Congress: 119
- Bill type: HRES
- Bill number: 1289
- Origin chamber: House
- Introduced date: 2026-05-14
- Update date: 2026-05-28T20:48:51Z
- Update date including text: 2026-05-28T20:48:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-05-14: Introduced in House
- 2026-05-14 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-05-14 - IntroReferral: Submitted in House
- Latest action: 2026-05-14: Submitted in House

## Actions

- 2026-05-14 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-05-14 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-14",
    "latestAction": {
      "actionDate": "2026-05-14",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1289",
    "number": "1289",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "T000481",
        "district": "12",
        "firstName": "Rashida",
        "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
        "lastName": "Tlaib",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Recognizing the ongoing Nakba and Palestinian refugees' rights.",
    "type": "HRES",
    "updateDate": "2026-05-28T20:48:51Z",
    "updateDateIncludingText": "2026-05-28T20:48:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-14",
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
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-05-14T14:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "IN"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "IL"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "TX"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "GA"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "PA"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MN"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "NY"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MN"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "IL"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "NJ"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-05-15",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1289ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1289\nIN THE HOUSE OF REPRESENTATIVES\nMay 14, 2026 Ms. Tlaib (for herself, Mr. Carson , Mr. Garc\u00eda of Illinois , Mr. Green of Texas , Mr. Johnson of Georgia , Ms. Lee of Pennsylvania , Ms. McCollum , Ms. Ocasio-Cortez , Ms. Omar , Ms. Pressley , Mrs. Ramirez , Ms. Simon , and Mrs. Watson Coleman ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nRecognizing the ongoing Nakba and Palestinian refugees\u2019 rights.\nThat it is the sense of the House of Representatives that it is the policy of the United States to\u2014\n**(1)**\ncommemorate the Nakba through official recognition and remembrance;\n**(2)**\ndenounce the ongoing Nakba of the Palestinian people;\n**(3)**\nreject efforts to enlist, engage, or otherwise associate the United States Government with denial of the Nakba;\n**(4)**\nencourage education and public understanding of the facts of the Nakba and the relevance of the Nakba to other modern-day refugee crises;\n**(5)**\nsupport the resumed provision of social services to Palestinian refugees through the United Nations Relief and Works Agency for Palestine Refugees in the Near East;\n**(6)**\nsupport the implementation of Palestinian refugees\u2019 rights as enshrined in United Nations General Assembly Resolution 194 and the Universal Declaration of Human Rights;\n**(7)**\nrecognize that Palestinians are a unique people who are every bit as human as everyone else;\n**(8)**\nreject bigoted efforts to question, dismiss, or otherwise deny the existence of Palestinians and their humanity; and\n**(9)**\nensure the United States ends its complicity in Israel\u2019s ongoing Nakba against the Palestinian people by\u2014\n**(A)**\nprohibiting United States weapons from being used to destroy Palestinian homes and forcibly remove Palestinians from their land; and\n**(B)**\nending United States diplomatic support for such actions.",
      "versionDate": "2026-05-14",
      "versionType": "IH"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-15",
        "text": "Sponsor introductory remarks on measure. (CR H2058)"
      },
      "number": "409",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Recognizing the ongoing Nakba and Palestinian refugees' rights.",
      "type": "HRES"
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
        "name": "International Affairs",
        "updateDate": "2026-05-28T20:48:51Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1289ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Recognizing the ongoing Nakba and Palestinian refugees' rights.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-15T08:18:27Z"
    },
    {
      "title": "Recognizing the ongoing Nakba and Palestinian refugees' rights.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T08:07:12Z"
    }
  ]
}
```
