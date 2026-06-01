# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2649?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2649
- Title: STOP Violence Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2649
- Origin chamber: House
- Introduced date: 2025-04-03
- Update date: 2025-10-18T08:05:32Z
- Update date including text: 2025-10-18T08:05:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-03: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-04-03: Introduced in House

## Actions

- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2649",
    "number": "2649",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "STOP Violence Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-18T08:05:32Z",
    "updateDateIncludingText": "2025-10-18T08:05:32Z"
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
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
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
          "date": "2025-04-03T15:03:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "NV"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "PA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "GA"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2649ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2649\nIN THE HOUSE OF REPRESENTATIVES\nApril 3, 2025 Mr. Neguse (for himself, Ms. Titus , and Ms. Dean of Pennsylvania ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to provide for additional grant amounts for protection against mass violence.\n#### 1. Short title\nThis Act may be cited as the Strengthen and Tackle Opportunities to Prevent Violence Act of 2025 or as the STOP Violence Act of 2025 .\n#### 2. Additional grant amounts for protection against mass violence\nSection 506 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10157 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1), by striking the and at the end;\n**(B)**\nin paragraph (2), by striking the period at the end and inserting ; and ; and\n**(C)**\nby inserting after paragraph (2) the following:\n(3) $20,000,000, to be granted by the Attorney General to States, units of local governments, and other nonprofit organizations that serve victims of crime to provide compensation, training, and technical assistance to public assembly facilities to prepare against mass violence and to protect public assembly facilities from mass violence. ; and\n**(2)**\nby adding at the end the following:\n(c) In this section: (1) The term mass violence includes active shooter incidents and targeted violence. (2) The term active shooter means an individual actively engaged in the unauthorized killing or attempting to kill a person or persons in a confined and populated area with a firearm. (3) The term target violence means an incident of violence where an assailant who is known or knowable to a law enforcement agency for a jurisdiction where the assailant resides, identifies a particular target prior to a violent attack, which may be one or more individuals, a class or category of individuals, or an institution, without regard to whether the assailant is able to successfully harm the chosen target. (4) The term public assembly facility means a permanent or temporary structure or facility, place, or activity where concentrations of people gather in reasonably close quarters for purposes including deliberation, education, worship, shopping, employment, entertainment, recreation, sporting events, or similar activities. .",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-01T13:25:35Z"
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
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2649ih.xml"
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
      "title": "STOP Violence Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-12T03:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "STOP Violence Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-12T03:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strengthen and Tackle Opportunities to Prevent Violence Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-12T03:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Omnibus Crime Control and Safe Streets Act of 1968 to provide for additional grant amounts for protection against mass violence.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-12T03:03:21Z"
    }
  ]
}
```
