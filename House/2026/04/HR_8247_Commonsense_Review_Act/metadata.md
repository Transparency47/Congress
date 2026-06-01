# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8247?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8247
- Title: Commonsense Review Act
- Congress: 119
- Bill type: HR
- Bill number: 8247
- Origin chamber: House
- Introduced date: 2026-04-13
- Update date: 2026-04-23T19:56:42Z
- Update date including text: 2026-04-23T19:56:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-13: Introduced in House
- 2026-04-13 - IntroReferral: Introduced in House
- 2026-04-13 - IntroReferral: Introduced in House
- 2026-04-13 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2026-04-13: Introduced in House

## Actions

- 2026-04-13 - IntroReferral: Introduced in House
- 2026-04-13 - IntroReferral: Introduced in House
- 2026-04-13 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-13",
    "latestAction": {
      "actionDate": "2026-04-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8247",
    "number": "8247",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
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
    "title": "Commonsense Review Act",
    "type": "HR",
    "updateDate": "2026-04-23T19:56:42Z",
    "updateDateIncludingText": "2026-04-23T19:56:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-13",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-13",
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
          "date": "2026-04-13T18:31:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8247ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8247\nIN THE HOUSE OF REPRESENTATIVES\nApril 13, 2026 Mr. Gottheimer (for himself and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo establish an interagency group on categorical exclusions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Commonsense Review Act .\n#### 2. Interagency group on categorical exclusions\n##### (a) Establishment\nThere is established an interagency group that shall work toward interagency alignment on categorical exclusions.\n##### (b) Membership\nThe interagency group established by subsection (a) shall consist of\u2014\n**(1)**\nthe Secretary of Energy;\n**(2)**\nthe Secretary of the Interior;\n**(3)**\neach member of the Federal Energy Regulatory Commission; and\n**(4)**\nthe Secretary of Agriculture.\n##### (c) Chair\nThe Secretary of Energy shall serve as the chair of the interagency group established by subsection (a).\n##### (d) Duties\nNot later than 360 days after the date of enactment of this Act, each member of the interagency group established by subsection (a) shall\u2014\n**(1)**\npursuant to section 109 of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4336c ), adopt any categorical exclusion with respect to which\u2014\n**(A)**\nthe member identifies the categorical exclusion under paragraph (1) of such section as listed in the NEPA procedures of another member of such interagency group; and\n**(B)**\nthe member ensures the adoption of such categorical exclusion to a category of actions is appropriate through consultation under paragraph (2) of such section; and\n**(2)**\njointly with another member of such interagency group, establish a new categorical exclusion for any category of actions relating to the interstate transmission of electric energy or to a battery energy storage project that such members determine normally does not significantly affect the quality of the human environment within the meaning of section 102(2)(C) of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4332(2)(C) ).\n##### (e) Report\nNot later than 360 days after the date of enactment of this Act, the interagency group established by subsection (a) shall submit to Congress a report on\u2014\n**(1)**\nany categorical exclusion that a member of the interagency group adopted or established pursuant to this section;\n**(2)**\nif any member of the interagency group did not adopt or establish a categorical exclusion pursuant to this section, the reason why the member did not take such action; and\n**(3)**\nany recommendations to Congress on\u2014\n**(A)**\nfuture areas for interagency collaboration on categorical exclusions; and\n**(B)**\nany need for a statutory categorical exclusion.\n##### (f) Sunset\nThe interagency group established by subsection (a) shall dissolve after submission of the report under subsection (e).",
      "versionDate": "2026-04-13",
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
        "name": "Environmental Protection",
        "updateDate": "2026-04-23T19:56:42Z"
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
      "date": "2026-04-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8247ih.xml"
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
      "title": "Commonsense Review Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T04:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Commonsense Review Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-16T04:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish an interagency group on categorical exclusions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-16T04:48:34Z"
    }
  ]
}
```
