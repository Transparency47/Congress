# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4883?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4883
- Title: Local Gun Violence Reduction Act
- Congress: 119
- Bill type: HR
- Bill number: 4883
- Origin chamber: House
- Introduced date: 2025-08-05
- Update date: 2025-09-18T19:24:52Z
- Update date including text: 2025-09-18T19:24:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-05: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-08-05: Introduced in House

## Actions

- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-05",
    "latestAction": {
      "actionDate": "2025-08-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4883",
    "number": "4883",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000623",
        "district": "10",
        "firstName": "Mark",
        "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
        "lastName": "DeSaulnier",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Local Gun Violence Reduction Act",
    "type": "HR",
    "updateDate": "2025-09-18T19:24:52Z",
    "updateDateIncludingText": "2025-09-18T19:24:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-05",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-05",
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
          "date": "2025-08-05T14:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4883ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4883\nIN THE HOUSE OF REPRESENTATIVES\nAugust 5, 2025 Mr. DeSaulnier introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Health and Human Services to establish and maintain a local gun violence prevention laws database, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Local Gun Violence Reduction Act .\n#### 2. Local gun violence prevention laws database\n##### (a) In general\nNot later than one year after the date of the enactment of this Act, the Secretary of Health and Human Services, acting through the Director of the Centers for Disease Control and Prevention (in this Act referred to as the Secretary ), shall establish and maintain a database in which units of State and local government (including cities, towns, counties, and special district governments) enter into such database information on\u2014\n**(1)**\nthe laws and ordinances such units of government have enacted to reduce gun violence; and\n**(2)**\nhow successful such laws and ordinances have been in reducing gun violence in the relevant jurisdictions.\n##### (b) Information\nThe information included by a State or local government in the database established under subsection (a) with respect to a law or ordinance referred to in such subsection shall include the following information:\n**(1)**\nInformation about the size of the unit of government involved.\n**(2)**\nThe date on which the law or ordinance was enacted.\n**(3)**\nThe date on which the law or ordinance took effect.\n**(4)**\nData on the rates of gun violence and gun deaths in the unit of government both before and after the law or ordinance took effect.\n##### (c) Access\nThe database established under subsection (a) shall be searchable by any State or local unit of government.\n##### (d) Outreach\nThe Secretary shall conduct outreach to State and local governments to increase awareness of the database under subsection (a) and to encourage such governments to use such database.\n##### (e) Report to Congress\nBeginning 2 years after the date of the enactment of this section, and every 2 years thereafter, the Secretary shall submit to Congress a report specifying, with respect to the database established under subsection (a)\u2014\n**(1)**\nhow many submissions to such database have been received;\n**(2)**\nwhat common topics are identified in such submissions;\n**(3)**\nwhich laws or ordinances the reports contained in such submissions indicate have been successful; and\n**(4)**\nany geographic areas within the United States that have high or low participation in the database.\n##### (f) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section\u2014\n**(1)**\n$1,500,000 for fiscal year 2026; and\n**(2)**\n$1,000,000 for fiscal year 2027 and each fiscal year thereafter.",
      "versionDate": "2025-08-05",
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
        "name": "Health",
        "updateDate": "2025-09-18T19:24:52Z"
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
      "date": "2025-08-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4883ih.xml"
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
      "title": "Local Gun Violence Reduction Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Local Gun Violence Reduction Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Health and Human Services to establish and maintain a local gun violence prevention laws database, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:48:35Z"
    }
  ]
}
```
