# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/176?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/176
- Title: 2026 Authorization for Use of Military Force Against Iran
- Congress: 119
- Bill type: HJRES
- Bill number: 176
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-12T19:47:40Z
- Update date including text: 2026-05-12T19:47:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-07: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2026-05-07: Introduced in House

## Actions

- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-07",
    "latestAction": {
      "actionDate": "2026-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/176",
    "number": "176",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "B001321",
        "district": "7",
        "firstName": "Tom",
        "fullName": "Rep. Barrett, Tom [R-MI-7]",
        "lastName": "Barrett",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "2026 Authorization for Use of Military Force Against Iran",
    "type": "HJRES",
    "updateDate": "2026-05-12T19:47:40Z",
    "updateDateIncludingText": "2026-05-12T19:47:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-07",
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
      "actionDate": "2026-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-07",
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
          "date": "2026-05-07T13:00:50Z",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hjres/BILLS-119hjres176ih.xml",
      "text": "IA\n119th CONGRESS\n2d Session\nH. J. RES. 176\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Mr. Barrett submitted the following joint resolution; which was referred to the Committee on Foreign Affairs\nJOINT RESOLUTION\nAuthorizing the use of the United States Armed Forces against the Government of the Islamic Republic of Iran.\n#### 1. Short title\nThis Joint Resolution may be cited as the 2026 Authorization for Use of Military Force Against Iran .\n#### 2. Authorization for use of United States Armed Forces\n##### (a) Authorization\nThe President is authorized to use the Armed Forces of the United States as the President determines to be necessary and appropriate in order to\u2014\n**(1)**\nsuccessfully demolish, degrade, or defeat the nuclear weapons program and associated delivery systems of the Government of the Islamic Republic of Iran;\n**(2)**\naddress imminent threats to the Armed Forces or to United States facilities posed by the Islamic Republic of Iran or Iranian-backed forces;\n**(3)**\nenforce a blockade of Iranian ports; and\n**(4)**\nensure safe passage for United States and allied vessels throughout the Strait of Hormuz, as well as any other vessels the President determines appropriate.\n##### (b) Limitations on use of ground troops\nThe authority granted in subsection (a) does not include any authorization for the deployment of the Armed Forces for the purpose of\u2014\n**(1)**\nconducting sustained ground combat operations in the territory of Iran;\n**(2)**\noccupying, seizing, or holding territory within Iran; or\n**(3)**\nengaging in nation-building, stabilization operations, or the establishment of long-term security governance within Iran.\n##### (c) Limited exceptions\nNothing in this section may be construed to prohibit the use of the Armed Forces for\u2014\n**(1)**\nthe rescue of United States citizens or members of the Armed Forces; or\n**(2)**\nintelligence collection or sharing activities in support of the national security of the United States, or in support of an ally or partner force.\n##### (d) War powers resolution requirements\n**(1) Specific statutory authorization**\nConsistent with section 8(a)(1) of the War Powers Resolution, the Congress declares that this section is intended to constitute specific statutory authorization within the meaning of section 5(b) of the War Powers Resolution.\n**(2) Applicability of other requirements**\nNothing in this joint resolution supersedes any requirement of the War Powers Resolution.\n#### 3. Report to Congress\n##### (a) In general\nThe President shall, at least once every 30 days, submit to Congress a report on matters relevant to this joint resolution, including\u2014\n**(1)**\nactions taken pursuant to the exercise of authority granted in section 2;\n**(2)**\na description of any military operations conducted in reliance on authorities other than the authority granted in section 2;\n**(3)**\nan explanation of the legal authority for each action and operation described in paragraphs (1) and (2);\n**(4)**\npolicy justifications for each action and operation described in paragraphs (1) and (2);\n**(5)**\nthe expected scope and duration of hostilities associated with each such action and operation; and\n**(6)**\nan assessment of civilian and military casualties.\n##### (b) Form\nThe report required by this section shall be submitted in unclassified form and may contain a classified annex.\n#### 4. Sunset\n##### (a) In general\nExcept as provided in subsection (b), the authority provided in section 2 shall terminate on July 30, 2026.\n##### (b) Limited wind-Down period\nFor an additional period of not more than 30 days after the date described in subsection (a), the authority provided in section 2 may be exercised only as necessary to end the deployment or engagement of the Armed Forces.",
      "versionDate": "2026-05-07",
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
        "name": "International Affairs",
        "updateDate": "2026-05-12T19:47:40Z"
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
      "date": "2026-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hjres/BILLS-119hjres176ih.xml"
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
      "title": "2026 Authorization for Use of Military Force Against Iran",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T08:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "2026 Authorization for Use of Military Force Against Iran",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T08:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Authorizing the use of the United States Armed Forces against the Government of the Islamic Republic of Iran.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T08:18:49Z"
    }
  ]
}
```
