# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/146?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/146
- Title: Proposing an amendment to the Constitution of the United States requiring Members of Congress to demonstrate competence in American civics.
- Congress: 119
- Bill type: HJRES
- Bill number: 146
- Origin chamber: House
- Introduced date: 2026-01-30
- Update date: 2026-02-02T14:41:54Z
- Update date including text: 2026-02-02T14:41:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-30: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-01-30: Introduced in House

## Actions

- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-30",
    "latestAction": {
      "actionDate": "2026-01-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/146",
    "number": "146",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "H001095",
        "district": "38",
        "firstName": "Wesley",
        "fullName": "Rep. Hunt, Wesley [R-TX-38]",
        "lastName": "Hunt",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Proposing an amendment to the Constitution of the United States requiring Members of Congress to demonstrate competence in American civics.",
    "type": "HJRES",
    "updateDate": "2026-02-02T14:41:54Z",
    "updateDateIncludingText": "2026-02-02T14:41:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-30",
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
      "actionDate": "2026-01-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-30",
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
          "date": "2026-01-30T15:30:15Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hjres/BILLS-119hjres146ih.xml",
      "text": "IA\n119th CONGRESS\n2d Session\nH. J. RES. 146\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 30, 2026 Mr. Hunt submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States requiring Members of Congress to demonstrate competence in American civics.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures or conventions of three-fourths of the several States:\n\u2014 1. The Congress shall establish, for each term of ten years for which a census or enumeration is conducted for the apportionment of the Representatives in the Congress, an examination for the demonstration of competence, to a standard expected for a citizen of the United States, on the system of government under the Constitution of the United States, and each House of the Congress shall publish the questions and answers for the examination in the Journal of its proceedings and choose such Officers who shall from time to time jointly and regularly administer the examination, which shall be without any cost to any person who takes the examination, and provide to any such person who demonstrates competence under the examination such certificates necessary to prove such demonstration. 2. No person shall be a Representative or Senator who shall not have demonstrated competence on the system of government under the Constitution of the United States under the examination in effect at the time of the election or appointment, but each House of Congress shall afford any person elected or appointed to be a Member of the House, without having demonstrated competence before the election or appointment, the opportunity to demonstrate such competence, whether under the same examination or by another means approved for such purpose by law. 3. The Congress shall have power to enforce this article by appropriate legislation, and such legislation shall not require the approval of the President before taking effect. .",
      "versionDate": "2026-01-30",
      "versionType": "IH"
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
        "name": "Congress",
        "updateDate": "2026-02-02T14:41:54Z"
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
      "date": "2026-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hjres/BILLS-119hjres146ih.xml"
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
      "title": "Proposing an amendment to the Constitution of the United States requiring Members of Congress to demonstrate competence in American civics.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-31T09:18:19Z"
    },
    {
      "title": "Proposing an amendment to the Constitution of the United States requiring Members of Congress to demonstrate competence in American civics.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-31T09:05:31Z"
    }
  ]
}
```
