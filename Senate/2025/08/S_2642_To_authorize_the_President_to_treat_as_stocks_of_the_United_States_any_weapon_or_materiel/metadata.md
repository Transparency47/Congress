# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2642?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2642
- Title: SEIZE Act
- Congress: 119
- Bill type: S
- Bill number: 2642
- Origin chamber: Senate
- Introduced date: 2025-08-01
- Update date: 2026-04-01T19:18:40Z
- Update date including text: 2026-04-01T19:18:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in Senate
- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-08-01: Introduced in Senate

## Actions

- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2642",
    "number": "2642",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "B001305",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Budd, Ted [R-NC]",
        "lastName": "Budd",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "SEIZE Act",
    "type": "S",
    "updateDate": "2026-04-01T19:18:40Z",
    "updateDateIncludingText": "2026-04-01T19:18:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-01",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-08-01T15:46:08Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2642is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2642\nIN THE SENATE OF THE UNITED STATES\nAugust 1, 2025 Mr. Budd (for himself and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo authorize the President to treat as stocks of the United States any weapon or materiel seized by the United States while in transit from the Islamic Republic of Iran to the Houthis in the Republic of Yemen.\n#### 1. Short title\nThis Act may be cited as the Seized Iranian Arms Transfer Authorization Act of 2025 or the SEIZE Act .\n#### 2. Disposition of weapons and materiel in transit from Iran to Houthis in Yemen\n##### (a) Disposition of weapons and materiel\nThe President may treat as stocks of the United States any weapon or materiel seized by the United States while in transit from the Islamic Republic of Iran to the Houthis in the Republic of Yemen.\n##### (b) Drawdown authority\nSection 506(a) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2318(a) ) is amended by adding at the end the following new paragraph:\n(4) In addition to amounts otherwise specified in this section, the President may direct the drawdown of weapons and materiel treated as stocks of the United States, seized pursuant to section 2(a) of the Seized Iranian Arms Transfer Authorization Act of 2025 , to be provided to foreign partners. .\n##### (c) Report\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter, the President shall submit to the appropriate committees of Congress a report that includes the following:\n**(1)**\nThe number of times the President exercised the authority under subsection (a).\n**(2)**\nAn inventory of the weapons and materiel treated as United States stocks pursuant to such authority.\n**(3)**\nAn inventory of the weapons and materiel provided to foreign partners pursuant to the authority provided in paragraph (4) of section 506(a) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2318(a) ).\n##### (d) Appropriate committees of Congress defined\nIn this section, the term appropriate committees of Congress means\u2014\n**(1)**\nthe Committee on Armed Services and the Committee on Foreign Relations of the Senate; and\n**(2)**\nthe Committee on Armed Services and the Committee on Foreign Affairs of the House of Representatives.",
      "versionDate": "2025-08-01",
      "versionType": "Introduced in Senate"
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
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-09-30",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "5623",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SEIZE Act of 2025",
      "type": "HR"
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
        "updateDate": "2025-09-11T18:52:31Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2642is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "SEIZE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-12T03:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SEIZE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Seized Iranian Arms Transfer Authorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the President to treat as stocks of the United States any weapon or material seized by the United States while in transit from the Islamic Republic of Iran to the Houthis in the Republic of Yemen.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-12T03:18:27Z"
    }
  ]
}
```
