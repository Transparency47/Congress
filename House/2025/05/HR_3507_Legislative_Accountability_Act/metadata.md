# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3507?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3507
- Title: Legislative Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 3507
- Origin chamber: House
- Introduced date: 2025-05-20
- Update date: 2026-02-04T04:11:36Z
- Update date including text: 2026-02-04T04:11:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-20: Introduced in House
- 2025-05-20 - IntroReferral: Introduced in House
- 2025-05-20 - IntroReferral: Introduced in House
- 2025-05-20 - IntroReferral: Referred to the Committee on Rules, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-20 - IntroReferral: Referred to the Committee on Rules, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-20: Introduced in House

## Actions

- 2025-05-20 - IntroReferral: Introduced in House
- 2025-05-20 - IntroReferral: Introduced in House
- 2025-05-20 - IntroReferral: Referred to the Committee on Rules, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-20 - IntroReferral: Referred to the Committee on Rules, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-20",
    "latestAction": {
      "actionDate": "2025-05-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3507",
    "number": "3507",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "B001309",
        "district": "2",
        "firstName": "Tim",
        "fullName": "Rep. Burchett, Tim [R-TN-2]",
        "lastName": "Burchett",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Legislative Accountability Act",
    "type": "HR",
    "updateDate": "2026-02-04T04:11:36Z",
    "updateDateIncludingText": "2026-02-04T04:11:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Rules, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-20",
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
      "text": "Referred to the Committee on Rules, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-20",
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
          "date": "2025-05-20T14:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-20T14:01:25Z",
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
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3507ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3507\nIN THE HOUSE OF REPRESENTATIVES\nMay 20, 2025 Mr. Burchett (for himself and Mr. Moskowitz ) introduced the following bill; which was referred to the Committee on Rules , and in addition to the Committee on House Administration , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the chairs of committees of the House of Representatives and the Senate to submit certain information to the Clerk of the House of Representatives or the Secretary of the Senate with respect to reported bills and joint resolutions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Legislative Accountability Act .\n#### 2. Requirements with respect to inclusion of certain information for bills and joint resolutions\n##### (a) Requirements with respect to certain amendments\n**(1) In general**\nWith respect to a bill or joint resolution reported by a committee of the House of Representatives or the Senate, the chair of such committee shall submit to the Clerk of the House of Representatives or the Secretary of the Senate (as the case may be), not later than 3 legislative days after the date that the bill or resolution is reported by the committee, the name of any Member of Congress who submitted an amendment to the bill or resolution which was adopted by the committee.\n**(2) Amendments adopted with respect to matters that pass either House**\nWith respect to a bill or joint resolution passed by the House of Representatives or the Senate, the chair of the Committee on Rules of the House or the Committee on Rules and Administration of the Senate shall submit to the Clerk of the House of Representatives or the Secretary of the Senate (as the case may be), not later than 3 legislative days after the date that the bill or resolution is passed by such House, the name of any Member of Congress who submitted an amendment to the bill or resolution which was adopted by such House.\n##### (b) Special rule with respect to matters reported by certain committees\nWith respect to a bill or joint resolution reported by the Committee on Appropriations of the House of Representatives or the Senate, the Committee on Ways and Means of the House, or the Committee on Finance of the Senate, the chair of such committee shall submit to the Clerk of the House of Representatives or the Secretary of the Senate (as the case may be), not later than 3 legislative days after the date that the bill or resolution is reported by the committee, the name of each Member of Congress who is responsible for the inclusion of a provision in the bill or resolution as reported by the committee.\n##### (c) Inclusion of certain information in bills or resolutions\nThe Clerk of the House of Representatives, the Secretary of the Senate (as the case may be), and the Director of the Government Publishing Office shall ensure that any name submitted under subsection (a) or (b) with respect to a bill or resolution is included in any reported, engrossed, enrolled or enacted version of the bill or resolution in the form of a footnote that indicates which adopted amendment or provision in the bill or resolution any such Member submitted for or is otherwise responsible for its inclusion in such version of the bill or resolution, as applicable.\n##### (d) Member of Congress defined\nIn this section, the term Member of Congress means a Senator or Representative in, or Delegate or Resident Commissioner to, the Congress.\n##### (e) Exercise of rulemaking powers\nThe provisions of this section are enacted by the Congress\u2014\n**(1)**\nas an exercise of the rulemaking power of the House of Representatives and the Senate, respectively, and as such they shall be considered as part of the rules of each House, respectively, or of that House to which they specifically apply, and such rules shall supersede other rules only to the extent that they are inconsistent therewith; and\n**(2)**\nwith full recognition of the constitutional right of either House to change such rules (so far as relating to such House) at any time, in the same manner, and to the same extent as in the case of any other rule of such House.",
      "versionDate": "2025-05-20",
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
        "name": "Congress",
        "updateDate": "2025-06-23T12:18:29Z"
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
      "date": "2025-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3507ih.xml"
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
      "title": "Legislative Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-28T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Legislative Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T03:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the chairs of committees of the House of Representatives and the Senate to submit certain information to the Clerk of the House of Representatives or the Secretary of the Senate with respect to reported bills and joint resolutions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T03:48:50Z"
    }
  ]
}
```
