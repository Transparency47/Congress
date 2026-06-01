# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6354?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6354
- Title: Cut the Burden, Keep the Benefits Act
- Congress: 119
- Bill type: HR
- Bill number: 6354
- Origin chamber: House
- Introduced date: 2025-12-02
- Update date: 2025-12-18T16:50:10Z
- Update date including text: 2025-12-18T16:50:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-02: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Referred to the House Committee on Small Business.
- Latest action: 2025-12-02: Introduced in House

## Actions

- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Referred to the House Committee on Small Business.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-02",
    "latestAction": {
      "actionDate": "2025-12-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6354",
    "number": "6354",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "C001123",
        "district": "31",
        "firstName": "Gilbert",
        "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
        "lastName": "Cisneros",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Cut the Burden, Keep the Benefits Act",
    "type": "HR",
    "updateDate": "2025-12-18T16:50:10Z",
    "updateDateIncludingText": "2025-12-18T16:50:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Small Business.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-02",
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
          "date": "2025-12-02T15:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
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
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "NY"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6354ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6354\nIN THE HOUSE OF REPRESENTATIVES\nDecember 2, 2025 Mr. Cisneros (for himself, Ms. Vel\u00e1zquez , and Ms. Scholten ) introduced the following bill; which was referred to the Committee on Small Business\nA BILL\nTo direct the Chief Counsel for Advocacy of the Small Business Administration to establish a hotline to receive notifications of burdensome Government actions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Cut the Burden, Keep the Benefits Act .\n#### 2. Establishment of hotline\nSection 203 of Public Law 94\u2013305 ( 15 U.S.C. 634c ) is amended by adding at the end the following new subsection:\n(c) Hotline (1) Establishment Not later than 180 days after the date of the enactment of this Act, the Chief Counsel for Advocacy shall\u2014 (A) operate and maintain an email address to be known as the Cut the Burden, Keep the Benefits Hotline (in this subsection referred to as the Hotline ) to receive notifications from small businesses, small organizations, and small governmental jurisdictions relating to Government actions affecting such small businesses, small organizations, or small governmental jurisdictions; (B) establish a website providing the email address or including a submission form or phone number in a manner that is easily accessible; and (C) solicit information from small businesses, small organizations, and small governmental jurisdictions related to Government actions, and when there is a notification related to a rule that will have a significant economic impact on a substantial number of small businesses, small organizations, or small governmental jurisdictions, or any combination thereof, consider regulatory alternatives that will achieve the goal of the agency with respect to such action while minimizing the burden on such entities. (2) Report Not later than 1 year after the date of the enactment of this subsection, and annually thereafter, the Chief Counsel for Advocacy shall submit to the Administrator of the Small Business Administration and Congress a report on the Hotline that includes\u2014 (A) the Government actions for which Hotline notifications are most frequently received, including the affected industry sectors for such Government actions; (B) for each such Government action that is a rule\u2014 (i) the dollar amount of the regulatory benefits of such rule as determined by\u2014 (I) the Director of the Office of Management and Budget in the most recent report containing an analysis of such rule submitted by the Director under section 624 of the Treasury and General Government Appropriations Act of 2001 ( Public Law 106\u2013554 ; 31 U.S.C. 1105 note); or (II) the agency that issued such rule; and (ii) if the dollar amount described in clause (i) is determined by the agency that issued such rule, a description by the agency of the regulatory benefits of such rule in qualitative or monetized terms; (C) for each such Government action that is related to an Executive order or Presidential proclamation that is related to tariffs\u2014 (i) the specific number of Hotline notifications; (ii) a summary of the costs imposted on small businesses, small organizations, and small governmental jurisdictions, including paperwork burdens and fees; and (iii) a summary of the actions taken by the Chief Counsel to address each such Government action; (D) a summary of all the Hotline notifications received, including, for each such Hotline notification, whether the notification is related to a rule or other Government action and the geographic area and the type of organization or affected industry from which the Hotline notification was sent; (E) an identification of\u2014 (i) each type of entity, disaggregated by small businesses, small organizations, small governmental jurisdictions, and representatives of such entities, that submitted a Hotline notification, and the rule for which each entity submitted such notification; and (ii) each Government action for which such entity submitted a Hotline notification; (F) recommendations for Government actions that minimize of such Government actions the burden on small businesses, small organizations, and small governmental jurisdictions; and (G) a summary of actions taken by the Chief Counsel to address the Government actions described in subparagraph (A) and the Hotline notifications described in subparagraph (D), including any such Government actions or notifications for which the Chief Counsel submitted comments or analyses. (3) Definitions In this subsection\u2014 (A) the term Government action means an action by the Federal Government, including rules, Executive orders, statutes, regulations, and Presidential proclamations; and (B) the terms rule , small business , small organization , and small governmental jurisdiction have the meanings given such terms, respectively, in section 601 of title 5, United States Code. .",
      "versionDate": "2025-12-02",
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
        "name": "Commerce",
        "updateDate": "2025-12-18T16:50:10Z"
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
      "date": "2025-12-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6354ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Chief Counsel for Advocacy of the Small Business Administration to establish a hotline to receive notifications of burdensome Government actions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-17T07:48:30Z"
    },
    {
      "title": "Cut the Burden, Keep the Benefits Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T07:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cut the Burden, Keep the Benefits Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T07:38:25Z"
    }
  ]
}
```
