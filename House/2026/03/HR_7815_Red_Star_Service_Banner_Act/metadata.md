# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7815?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7815
- Title: Red Star Service Banner Act
- Congress: 119
- Bill type: HR
- Bill number: 7815
- Origin chamber: House
- Introduced date: 2026-03-05
- Update date: 2026-04-01T20:19:18Z
- Update date including text: 2026-04-01T20:19:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-03-05: Introduced in House

## Actions

- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7815",
    "number": "7815",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001301",
        "district": "1",
        "firstName": "Jack",
        "fullName": "Rep. Bergman, Jack [R-MI-1]",
        "lastName": "Bergman",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Red Star Service Banner Act",
    "type": "HR",
    "updateDate": "2026-04-01T20:19:18Z",
    "updateDateIncludingText": "2026-04-01T20:19:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-05",
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
      "actionDate": "2026-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-05",
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
          "date": "2026-03-05T15:04:15Z",
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
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "FL"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "FL"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7815ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7815\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2026 Mr. Bergman (for himself, Mr. Correa , Mr. Bilirakis , Mrs. Luna , Mr. Bost , and Mr. Dunn of Florida ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 36, United States Code, to establish the Red Star Service Banner as an officially recognized service banner, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Red Star Service Banner Act .\n#### 2. Establishment of the Red Star Service Banner\n##### (a) In general\nChapter 9 of title 36, United States Code, is amended by adding at the end the following new section:\n905. Red Star Service Banner (a) Designation The Red Star Service Banner is designated as a commemorative symbol\u2014 (1) recognizing and remembering the service members and veterans of the United States who have died by suicide; and (2) acknowledging the enduring sacrifice of their families. (b) Design The Red Star Service Banner shall consist of a white field with a blue border and a single red star centered within the field, as approved by the Secretary of Veterans Affairs. (c) Display The Red Star Service Banner may be displayed\u2014 (1) at the place of residence of a member of the immediate family of a service member or veteran who has died by suicide; (2) within the office or building of a veterans service organization or any similar entity that supports service members, veterans, and their families; (3) in the workplace or place of business of a member of the immediate family of a service member or veteran who has died by suicide, or in any business establishment that chooses to honor the memory of service members and veterans who have died by suicide; (4) in public buildings, including Federal, State, Tribal, and local government facilities, when displayed as part of a program, ceremony, or installation intended to recognize and support service members, veterans, and their families; (5) in community spaces open to the public, including schools, libraries, places of worship, and civic centers, when used to promote awareness of the sacrifices of service members and veterans and to support surviving families; and (6) at any other appropriate location, public or private, where the display serves to honor the memory of service members and veterans who have died by suicide. (d) Relation to other service banners The Red Star Service Banner may be displayed alongside other officially recognized service banners. (e) Public awareness The Secretary of Veterans Affairs, in coordination with the Secretary of Defense, may take appropriate actions to promote public awareness and understanding of the Red Star Service Banner. (f) First responders The Red Star Service Banner may also be displayed to honor the memory of a first responder who has died by suicide, including first responders such as firefighters, law enforcement officers, and emergency medical personnel, and may be displayed at the place of residence, workplace, or place of business of a member of the immediate family of such a first responder or in any other locations that bear the same relationship to first responders as the locations described in subsection (c) bear to service members and veterans. (g) Rule of construction Nothing in this section shall be construed to\u2014 (1) establish eligibility for, or entitlement to, any benefit, program, or assistance administered by the Department of Veterans Affairs or any other Federal agency; (2) require the Department of Veterans Affairs to administer, certify, or approve individual eligibility for display of the Red Star Service Banner; or (3) create any legal status, designation, or classification for purposes of Federal law other than recognition under this chapter. .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 9 of such title is amended by adding at the end the following:\n905. Red Star Service Banner. .\n#### 3. No additional appropriations\nNo additional funds are authorized to be appropriated to carry out the amendments made by this Act, and the amendments made by this Act shall be carried out using amounts otherwise made available to the Department of Veterans Affairs.",
      "versionDate": "2026-03-05",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-04-01T20:19:18Z"
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
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7815ih.xml"
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
      "title": "Red Star Service Banner Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T06:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Red Star Service Banner Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T06:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 36, United States Code, to establish the Red Star Service Banner as an officially recognized service banner, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-24T06:48:34Z"
    }
  ]
}
```
