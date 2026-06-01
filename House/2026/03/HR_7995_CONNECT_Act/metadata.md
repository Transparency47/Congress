# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7995?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7995
- Title: CONNECT Act
- Congress: 119
- Bill type: HR
- Bill number: 7995
- Origin chamber: House
- Introduced date: 2026-03-19
- Update date: 2026-05-30T17:41:23Z
- Update date including text: 2026-05-30T17:41:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2026-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-29 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 40 - 0.
- 2026-05-11 - Calendars: Placed on the Union Calendar, Calendar No. 559.
- 2026-05-11 - Committee: Reported (Amended) by the Committee on Ways and Means. H. Rept. 119-642.
- 2026-05-11 - Committee: Reported (Amended) by the Committee on Ways and Means. H. Rept. 119-642.
- Latest action: 2026-03-19: Introduced in House

## Actions

- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2026-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-29 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 40 - 0.
- 2026-05-11 - Calendars: Placed on the Union Calendar, Calendar No. 559.
- 2026-05-11 - Committee: Reported (Amended) by the Committee on Ways and Means. H. Rept. 119-642.
- 2026-05-11 - Committee: Reported (Amended) by the Committee on Ways and Means. H. Rept. 119-642.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7995",
    "number": "7995",
    "originChamber": "House",
    "policyArea": {
      "name": "Families"
    },
    "sponsors": [
      {
        "bioguideId": "M001160",
        "district": "4",
        "firstName": "Gwen",
        "fullName": "Rep. Moore, Gwen [D-WI-4]",
        "lastName": "Moore",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "CONNECT Act",
    "type": "HR",
    "updateDate": "2026-05-30T17:41:23Z",
    "updateDateIncludingText": "2026-05-30T17:41:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2026-05-11",
      "calendarNumber": {
        "calendar": "U00559"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 559.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2026-05-11",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Reported (Amended) by the Committee on Ways and Means. H. Rept. 119-642.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2026-05-11",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Ways and Means. H. Rept. 119-642.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 40 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-19",
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
        "item": [
          {
            "date": "2026-05-11T15:17:09Z",
            "name": "Reported By"
          },
          {
            "date": "2026-04-29T14:50:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-03-19T13:04:05Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "OH"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "IL"
    },
    {
      "bioguideId": "S001183",
      "district": "1",
      "firstName": "David",
      "fullName": "Rep. Schweikert, David [R-AZ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Schweikert",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7995ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7995\nIN THE HOUSE OF REPRESENTATIVES\nMarch 19, 2026 Ms. Moore of Wisconsin (for herself and Mr. Carey ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo update the purposes of the John H. Chafee Foster Care Program for Successful Transition to Adulthood to reflect research and the input of youth with lived experience about the importance of long-term relationships to future success.\n#### 1. Short title\nThis Act may be cited as the Chafee Opportunities for New Networks and Existing Connection Trust Act or the CONNECT Act .\n#### 2. Updating the purposes of the John H. Chafee Foster Care Program for Successful Transition to Adulthood\n##### (a) Updating of purposes\n**(1) In general**\nSection 477(a) of the Social Security Act ( 42 U.S.C. 677(a) ) is amended\u2014\n**(A)**\nby striking paragraph (2);\n**(B)**\nby redesignating paragraphs (1) and (3) through (7) as paragraphs (3) through (8), respectively; and\n**(C)**\nby inserting after conducted\u2014 the following:\n(1) to help children who have experienced foster care at age 14 or older to develop and maintain sustained, supportive relationships with adults (including kin or fictive kin who are not serving as placement), mentors, and peers (including peers who have experienced foster care), with a goal of providing multiple and varied paths to reduce isolation and ensuring that the youth develop lifelong connections and support networks; (2) to support youth still in foster care who have experienced foster care at age 14 or older in exercising the rights referred to in section 475A to participate in developing their permanency plan and receive written information about available services and steps the agency is taking to support the plan, as well as to facilitate pre- and post-permanency peer support, mentoring, connections with kin, and referrals to additional appropriate programs and services to help youth achieve their permanency goals; .\n**(2) Effective date**\nThe amendments made by paragraph (1) shall take effect on the date that is 1 year after the date of the enactment of this Act.\n##### (b) Guidance\nWithin 1 year after the date of the enactment of this Act and after consulting with youth with lived experience in foster care, the Secretary of Health and Human Services shall issue guidance to States and Tribal child welfare agencies, regarding the purposes set forth in paragraphs (1) and (2) of section 477(a) of the Social Security Act, that includes, at a minimum\u2014\n**(1)**\nexamples of services and support eligible for Federal funding under part B of title IV of such Act, under part E of such title as part of completing and following the case plan requirements provided for in section 475A of such Act, or under section 477 of such Act, including individual youth support, family support, and peer support to engage youth during reunification, guardianship, or adoption proceedings;\n**(2)**\nbest practices for facilitating peer support, mentoring, and the development and maintenance of lifelong connections, including practices that support sibling, tribal, and community connections, including minimum qualifications and training for persons providing mentoring and peer support;\n**(3)**\nstandards of outreach to and notification of eligible youth, including youth with a planned permanent living arrangement, to ensure referrals to appropriate programs and services; and\n**(4)**\nprotocols for documentation of support and relationship-building activities under section 477 of such Act that are required by section 475A of such Act to be included in a child's case plan, sufficient to permit review under the case review system described in section 475(5) of such Act.",
      "versionDate": "2026-03-19",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7995rh.xml",
      "text": "IB\nUnion Calendar No. 559\n119th CONGRESS\n2d Session\nH. R. 7995\n[Report No. 119\u2013642]\nIN THE HOUSE OF REPRESENTATIVES\nMarch 19, 2026 Ms. Moore of Wisconsin (for herself and Mr. Carey ) introduced the following bill; which was referred to the Committee on Ways and Means\nMay 11, 2026 Additional sponsors: Mr. Davis of Illinois and Mr. Schweikert\nMay 11, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as printed in the House of Representatives on March 19, 2026\nA BILL\nTo update the purposes of the John H. Chafee Foster Care Program for Successful Transition to Adulthood to reflect research and the input of youth with lived experience about the importance of long-term relationships to future success.\n#### 1. Short title\nThis Act may be cited as the Chafee Opportunities for New Networks and Existing Connection Trust Act or the CONNECT Act .\n#### 2. Updating the purposes of the John H. Chafee Foster Care Program for Successful Transition to Adulthood\n##### (a) Updating of purposes\n**(1) In general**\nSection 477(a) of the Social Security Act ( 42 U.S.C. 677(a) ) is amended\u2014\n**(A)**\nby striking paragraph (2);\n**(B)**\nby redesignating paragraphs (1) and (3) through (7) as paragraphs (3) through (8), respectively; and\n**(C)**\nby inserting after conducted\u2014 the following:\n(1) to help children who have experienced foster care at age 14 or older to develop and maintain sustained, supportive relationships with adults (including kin or fictive kin who are not serving as placement), mentors, and peers (including peers who have experienced foster care), with a goal of providing multiple and varied paths to reduce isolation and ensuring that the youth develop lifelong connections and support networks; (2) to support youth still in foster care who have experienced foster care at age 14 or older in exercising the rights referred to in section 475A to participate in developing their permanency plan and receive written information about available services and steps the agency is taking to support the plan, as well as to facilitate pre- and post-permanency peer support, mentoring, connections with kin, and referrals to additional appropriate programs and services to help youth achieve their permanency goals; .\n**(2) Effective date**\nThe amendments made by paragraph (1) shall take effect on the date that is 1 year after the date of the enactment of this Act.\n##### (b) Guidance\nWithin 1 year after the date of the enactment of this Act and after consulting with youth with lived experience in foster care, the Secretary of Health and Human Services shall issue guidance to States and Tribal child welfare agencies regarding the purposes set forth in paragraphs (1) and (2) of section 477(a) of the Social Security Act, that includes, at a minimum\u2014\n**(1)**\nexamples of services and support eligible for Federal funding under part B of title IV of such Act, under part E of such title as part of completing and following the case plan requirements provided for in section 475A of such Act, or under section 477 of such Act, including individual youth support, family support, and peer support to engage youth during reunification, guardianship, or adoption proceedings;\n**(2)**\nbest practices for facilitating peer support, mentoring, and the development and maintenance of lifelong connections, including practices that support sibling, tribal, and community connections, including minimum qualifications and training for persons providing mentoring and peer support;\n**(3)**\nstandards of outreach to and notification of eligible youth, including youth with a planned permanent living arrangement, to ensure referrals to appropriate programs and services; and\n**(4)**\nprotocols for documentation of support and relationship-building activities under section 477 of such Act that are required by section 475A of such Act to be included in a child's case plan, sufficient to permit review under the case review system described in section 475(5) of such Act.",
      "versionDate": "2026-05-11",
      "versionType": "Reported in House"
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
        "actionDate": "2026-05-20",
        "text": "Received in the Senate and Read twice and referred to the Committee on Finance."
      },
      "number": "7432",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Fostering the Future Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Adoption and foster care",
            "updateDate": "2026-05-11T15:59:01Z"
          },
          {
            "name": "Child care and development",
            "updateDate": "2026-05-11T15:59:07Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2026-05-11T15:59:17Z"
          },
          {
            "name": "Family services",
            "updateDate": "2026-05-11T15:59:12Z"
          }
        ]
      },
      "policyArea": {
        "name": "Families",
        "updateDate": "2026-05-18T20:50:22Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7995ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-05-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7995rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "CONNECT Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-05-12T05:53:25Z"
    },
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Chafee Opportunities for New Networks and Existing Connection Trust Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-05-12T05:53:25Z"
    },
    {
      "title": "CONNECT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T08:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CONNECT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T08:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Chafee Opportunities for New Networks and Existing Connection Trust Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T08:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To update the purposes of the John H. Chafee Foster Care Program for Successful Transition to Adulthood to reflect research and the input of youth with lived experience about the importance of long-term relationships to future success.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T08:18:26Z"
    }
  ]
}
```
