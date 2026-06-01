# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1034?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1034
- Title: Relating to questions of privilege in the House of Representatives during the One Hundred Nineteenth Congress.
- Congress: 119
- Bill type: HRES
- Bill number: 1034
- Origin chamber: House
- Introduced date: 2026-02-03
- Update date: 2026-02-06T16:50:44Z
- Update date including text: 2026-02-06T16:50:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-03: Introduced in House
- 2026-02-03 - IntroReferral: Referred to the House Committee on Rules.
- 2026-02-03 - IntroReferral: Submitted in House
- 2026-02-03 - IntroReferral: Submitted in House
- Latest action: 2026-02-03: Submitted in House

## Actions

- 2026-02-03 - IntroReferral: Referred to the House Committee on Rules.
- 2026-02-03 - IntroReferral: Submitted in House
- 2026-02-03 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-03",
    "latestAction": {
      "actionDate": "2026-02-03",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1034",
    "number": "1034",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "J000301",
        "district": "",
        "firstName": "Dusty",
        "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
        "lastName": "Johnson",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Relating to questions of privilege in the House of Representatives during the One Hundred Nineteenth Congress.",
    "type": "HRES",
    "updateDate": "2026-02-06T16:50:44Z",
    "updateDateIncludingText": "2026-02-06T16:50:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-03",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Rules.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-02-03",
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
          "date": "2026-02-03T15:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "VA"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "KS"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "IN"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "MT"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "CO"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "NC"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "KS"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "NC"
    },
    {
      "bioguideId": "G000558",
      "district": "2",
      "firstName": "Brett",
      "fullName": "Rep. Guthrie, Brett [R-KY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Guthrie",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "KY"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "NE"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1034ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1034\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 3, 2026 Mr. Johnson of South Dakota (for himself, Mr. Griffith , Mr. Mann , Mr. Baird , Mr. Downing , Mr. Hurd of Colorado , Mr. Harrigan , Mr. Schmidt , Mr. Rouzer , Mr. Guthrie , and Mr. Bacon ) submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nRelating to questions of privilege in the House of Representatives during the One Hundred Nineteenth Congress.\n#### 1. Questions of privilege in the House of Representatives\n##### (a) In general\nDuring the remainder of the One Hundred Nineteenth Congress in the House of Representatives, notwithstanding clause 2(a)(1) of rule IX of the Rules of the House, with respect to a resolution described in subsection (c) , the Chair may not entertain\u2014\n**(1)**\nany such resolution offered by the Majority Leader or the Minority Leader unless the resolution has accumulated one-fifth of the total membership of the House as cosponsors at the time it is offered; or\n**(2)**\nan announcement by a Member, Delegate, or Resident Commissioner of an intention to offer any such resolution unless the resolution has maintained at least one-fifth of the total membership of the House as cosponsors for at least one legislative day after its introduction.\n##### (b) Oral announcement\nOral announcement of the form of a resolution referred to in subsection (a) shall be considered as dispensed with.\n##### (c) Resolution described\nA resolution described in this subsection is a resolution offered from the floor of the House of Representatives as a question of the privileges of the House addressing the conduct of any Member, Delegate, or Resident Commissioner, but does not include a resolution described in clause 2(a)(3) of rule IX of the Rules of the House.",
      "versionDate": "2026-02-03",
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
        "updateDate": "2026-02-06T16:50:43Z"
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
      "date": "2026-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1034ih.xml"
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
      "title": "Relating to questions of privilege in the House of Representatives during the One Hundred Nineteenth Congress.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-04T09:18:19Z"
    },
    {
      "title": "Relating to questions of privilege in the House of Representatives during the One Hundred Nineteenth Congress.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-04T09:06:56Z"
    }
  ]
}
```
