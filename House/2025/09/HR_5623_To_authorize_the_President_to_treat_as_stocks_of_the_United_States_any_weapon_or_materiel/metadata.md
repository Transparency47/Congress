# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5623?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5623
- Title: SEIZE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5623
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2026-04-10T14:53:01Z
- Update date including text: 2026-04-10T14:53:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-09-30: Introduced in House

## Actions

- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5623",
    "number": "5623",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "SEIZE Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-10T14:53:01Z",
    "updateDateIncludingText": "2026-04-10T14:53:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:04:35Z",
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
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "IN"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "FL"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "GA"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "FL"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5623ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5623\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Mr. Gottheimer (for himself, Mr. Shreve , Mr. Moskowitz , Mr. McCormick , and Ms. Wasserman Schultz ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo authorize the President to treat as stocks of the United States any weapon or materiel seized by the United States while in transit from the Islamic Republic of Iran to the Houthis in the Republic of Yemen.\n#### 1. Short title\nThis Act may be cited as the Seized Iranian Arms Transfer Authorization Act of 2025 or the SEIZE Act of 2025 .\n#### 2. Disposition of weapons and materiel in transit from Iran to Houthis in Yemen\n##### (a) Disposition of weapons and materiel\nThe President may treat as stocks of the United States any weapon or materiel seized by the United States while in transit from the Islamic Republic of Iran to the Houthis in the Republic of Yemen.\n##### (b) Drawdown authority\nSection 506(a) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2318(a) ) is amended by adding at the end the following new paragraph:\n(4) In addition to amounts otherwise specified in this section, the President may direct the drawdown of weapons and materiel treated as stocks of the United States, seized pursuant to section 2(a) of the Seized Iranian Arms Transfer Authorization Act of 2025 , to be provided to foreign partners. .\n##### (c) Report\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter, the President shall submit to the appropriate committees of Congress a report that includes the following:\n**(1)**\nThe number of times the President exercised the authority under subsection (a).\n**(2)**\nAn inventory of the weapons and materiel treated as United States stocks pursuant to such authority.\n**(3)**\nAn inventory of the weapons and materiel provided to foreign partners pursuant to the authority provided in paragraph (4) of section 506(a) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2318(a) ).\n##### (d) Appropriate committees of Congress defined\nIn this section, the term appropriate committees of Congress means\u2014\n**(1)**\nthe Committee on Armed Services and the Committee on Foreign Relations of the Senate; and\n**(2)**\nthe Committee on Armed Services and the Committee on Foreign Affairs of the House of Representatives.",
      "versionDate": "2025-09-30",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-08-01",
        "text": "Read twice and referred to the Committee on Foreign Relations."
      },
      "number": "2642",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SEIZE Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-11-12",
        "actionTime": "12:10:52",
        "text": "Held at the desk."
      },
      "number": "2296",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
      "type": "S"
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
        "updateDate": "2025-11-20T16:08:05Z"
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5623ih.xml"
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
      "title": "SEIZE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-09T04:53:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SEIZE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-09T04:53:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Seized Iranian Arms Transfer Authorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-09T04:53:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the President to treat as stocks of the United States any weapon or materiel seized by the United States while in transit from the Islamic Republic of Iran to the Houthis in the Republic of Yemen.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-09T04:48:20Z"
    }
  ]
}
```
