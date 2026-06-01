# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4846?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4846
- Title: ROAD Act
- Congress: 119
- Bill type: HR
- Bill number: 4846
- Origin chamber: House
- Introduced date: 2025-08-01
- Update date: 2025-09-18T18:09:41Z
- Update date including text: 2025-09-18T18:09:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-08-01: Introduced in House

## Actions

- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the House Committee on the Judiciary.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4846",
    "number": "4846",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "F000484",
        "district": "6",
        "firstName": "Randy",
        "fullName": "Rep. Fine, Randy [R-FL-6]",
        "lastName": "Fine",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "ROAD Act",
    "type": "HR",
    "updateDate": "2025-09-18T18:09:41Z",
    "updateDateIncludingText": "2025-09-18T18:09:41Z"
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
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-01",
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
          "date": "2025-08-01T14:07:15Z",
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
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "TX"
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
      "sponsorshipDate": "2025-09-11",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4846ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4846\nIN THE HOUSE OF REPRESENTATIVES\nAugust 1, 2025 Mr. Fine introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to provide for an affirmative defense in a criminal or civil action relating to motor vehicle incidents if cases in which a certain party is convicted of riot.\n#### 1. Short title\nThis Act may be cited as the Reinstating Orderly Access for Drivers Act or the ROAD Act .\n#### 2. Affirmative defense in a criminal or civil action; party convicted of riot\n##### (a) In general\nChapter 2 of title 18, United States Code, is amended by adding at the end the following:\n40B. Affirmative defense in a criminal or civil action; party convicted of riot (a) In a criminal or civil action for damages for personal injury, wrongful death, or property damage carried out using a motor vehicle, it is an affirmative defense that such action arose from an injury or damage sustained by a participant acting in furtherance of a riot. The affirmative defense authorized by this section shall be established by evidence that the participant has been convicted of violating section 2101, or by proof of the commission of such crime by a preponderance of the evidence. (b) In a civil action in which a defendant raises an affirmative defense under this section, the court shall, on motion by the defendant, stay the action during the pendency of a criminal action that forms the basis for the defense, unless the court finds that a conviction in the criminal action would not form a valid defense under this section. .\n##### (b) Clerical amendment\nThe analysis for chapter 2 of title 18, United States Code, is amended by adding at the end the following:\n40B. Affirmative defense in a criminal or civil action; party convicted of riot. .",
      "versionDate": "2025-08-01",
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
        "updateDate": "2025-09-18T18:09:41Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4846ih.xml"
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
      "title": "ROAD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ROAD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reinstating Orderly Access for Drivers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to provide for an affirmative defense in a criminal or civil action relating to motor vehicle incidents if cases in which a certain party is convicted of riot.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:45Z"
    }
  ]
}
```
