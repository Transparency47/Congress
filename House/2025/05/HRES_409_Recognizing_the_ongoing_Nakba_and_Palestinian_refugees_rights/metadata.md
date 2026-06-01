# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/409?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/409
- Title: Recognizing the ongoing Nakba and Palestinian refugees' rights.
- Congress: 119
- Bill type: HRES
- Bill number: 409
- Origin chamber: House
- Introduced date: 2025-05-14
- Update date: 2026-05-28T20:48:43Z
- Update date including text: 2026-05-28T20:48:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-14: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-05-14 - IntroReferral: Submitted in House
- 2025-05-14 - IntroReferral: Submitted in House
- 2025-05-15 - IntroReferral: Sponsor introductory remarks on measure. (CR H2058)
- Latest action: 2025-05-14: Submitted in House

## Actions

- 2025-05-14 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-05-14 - IntroReferral: Submitted in House
- 2025-05-14 - IntroReferral: Submitted in House
- 2025-05-15 - IntroReferral: Sponsor introductory remarks on measure. (CR H2058)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/409",
    "number": "409",
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
    "updateDate": "2026-05-28T20:48:43Z",
    "updateDateIncludingText": "2026-05-28T20:48:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H2058)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-14",
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
      "actionCode": "H11100",
      "actionDate": "2025-05-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-14",
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
          "date": "2025-05-14T14:03:30Z",
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
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "PA"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "MN"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "NY"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "NJ"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
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
      "sponsorshipDate": "2025-05-14",
      "state": "IL"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres409ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 409\nIN THE HOUSE OF REPRESENTATIVES\nMay 14, 2025 Ms. Tlaib (for herself, Ms. Lee of Pennsylvania , Ms. Omar , Ms. Simon , Ms. Ocasio-Cortez , Mrs. Watson Coleman , Ms. Pressley , Mrs. Ramirez , and Mr. Carson ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nRecognizing the ongoing Nakba and Palestinian refugees\u2019 rights.\nThat it is the sense of the House of Representatives that it is the policy of the United States to\u2014\n**(1)**\ncommemorate the Nakba through official recognition and remembrance;\n**(2)**\ndenounce the ongoing Nakba of the Palestinian people;\n**(3)**\nreject efforts to enlist, engage, or otherwise associate the United States Government with denial of the Nakba;\n**(4)**\nencourage education and public understanding of the facts of the Nakba, including the United States role in the humanitarian relief effort, and the relevance of the Nakba to modern-day refugee crises;\n**(5)**\nsupport the resumed provision of social services to Palestinian refugees through the United Nations Relief and Works Agency for Palestine Refugees in the Near East;\n**(6)**\nsupport the implementation of Palestinian refugees\u2019 rights as enshrined in United Nations General Assembly Resolution 194 and the Universal Declaration of Human Rights;\n**(7)**\nrecognize that Palestinians are a unique people who are every bit as human as everyone else;\n**(8)**\nreject bigoted efforts to question, dismiss, or otherwise deny the existence of Palestinians and their humanity; and\n**(9)**\nensure the United States ends its complicity in Israel\u2019s ongoing Nakba against the Palestinian people by\u2014\n**(A)**\nprohibiting United States weapons from being used to destroy Palestinian homes and forcibly remove Palestinians from their land; and\n**(B)**\nending United States diplomatic support for such actions.",
      "versionDate": "2025-05-14",
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
        "actionDate": "2026-05-14",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "1289",
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
        "updateDate": "2025-06-09T14:34:04Z"
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
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres409ih.xml"
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
      "updateDate": "2025-05-15T09:36:17Z"
    },
    {
      "title": "Recognizing the ongoing Nakba and Palestinian refugees' rights.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-15T08:11:12Z"
    }
  ]
}
```
