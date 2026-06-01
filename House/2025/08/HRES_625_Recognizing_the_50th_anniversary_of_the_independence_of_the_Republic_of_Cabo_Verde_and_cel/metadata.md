# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/625?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/625
- Title: Recognizing the 50th anniversary of the independence of the Republic of Cabo Verde and celebrating the contributions of Cabo Verdean-Americans to democracy in Cabo Verde and the United States.
- Congress: 119
- Bill type: HRES
- Bill number: 625
- Origin chamber: House
- Introduced date: 2025-08-01
- Update date: 2026-04-01T21:12:24Z
- Update date including text: 2026-04-01T21:12:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-08-01 - IntroReferral: Submitted in House
- 2025-08-01 - IntroReferral: Submitted in House
- Latest action: 2025-08-01: Submitted in House

## Actions

- 2025-08-01 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-08-01 - IntroReferral: Submitted in House
- 2025-08-01 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/625",
    "number": "625",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "J000294",
        "district": "8",
        "firstName": "Hakeem",
        "fullName": "Rep. Jeffries, Hakeem S. [D-NY-8]",
        "lastName": "Jeffries",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Recognizing the 50th anniversary of the independence of the Republic of Cabo Verde and celebrating the contributions of Cabo Verdean-Americans to democracy in Cabo Verde and the United States.",
    "type": "HRES",
    "updateDate": "2026-04-01T21:12:24Z",
    "updateDateIncludingText": "2026-04-01T21:12:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-01",
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
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-08-01",
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
          "date": "2025-08-01T14:03:10Z",
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
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "CT"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "MA"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "NY"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "NY"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "MA"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "NV"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "MA"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "CA"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "FL"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "IL"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "CA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "RI"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres625ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 625\nIN THE HOUSE OF REPRESENTATIVES\nAugust 1, 2025 Mr. Jeffries (for himself, Ms. DeLauro , Mr. McGovern , Mr. Meeks , Ms. Clarke of New York , Mr. Keating , Mr. Horsford , Ms. Pressley , Ms. Jacobs , Mrs. Cherfilus-McCormick , Mr. Jackson of Illinois , Ms. Kamlager-Dove , Mr. Magaziner , and Mr. Amo ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nRecognizing the 50th anniversary of the independence of the Republic of Cabo Verde and celebrating the contributions of Cabo Verdean-Americans to democracy in Cabo Verde and the United States.\nThat the House of Representatives\u2014\n**(1)**\nextends sincere congratulations and best wishes to the people of the Republic of Cabo Verde as they celebrate the 50th anniversary of the independence of the archipelago of Cabo Verde;\n**(2)**\nexpresses support for the principles of freedom, democracy, and good governance, to which the people and Government of the Republic of Cabo Verde are committed;\n**(3)**\ncommends the Cabo Verdean-American community for its contributions to the United States and service as a bridge between the two countries, both before and following independence, based on shared bilateral history, diasporic ties, and common values;\n**(4)**\nnotes the important role that the Republic of Cabo Verde has played in African and broader transatlantic affairs since gaining independence on July 5, 1975; and\n**(5)**\ncommends the Republic of Cabo Verde\u2019s support for the sovereignty, territorial integrity, and people of Ukraine, and its condemnation of the invasion of Ukraine by Russia.",
      "versionDate": "2025-08-01",
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
        "actionDate": "2025-09-04",
        "text": "Referred to the Committee on Foreign Relations. (text: CR S6329-6330)"
      },
      "number": "373",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution recognizing the 50th anniversary of the independence of the Republic of Cabo Verde and celebrating the contributions of Cabo Verdean-Americans to democracy in Cabo Verde and the United States.",
      "type": "SRES"
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
        "updateDate": "2025-09-11T21:40:35Z"
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
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres625ih.xml"
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
      "title": "Recognizing the 50th anniversary of the independence of the Republic of Cabo Verde and celebrating the contributions of Cabo Verdean-Americans to democracy in Cabo Verde and the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-02T08:18:18Z"
    },
    {
      "title": "Recognizing the 50th anniversary of the independence of the Republic of Cabo Verde and celebrating the contributions of Cabo Verdean-Americans to democracy in Cabo Verde and the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-02T08:05:35Z"
    }
  ]
}
```
