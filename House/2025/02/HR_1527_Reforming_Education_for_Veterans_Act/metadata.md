# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1527?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1527
- Title: Reforming Education for Veterans Act
- Congress: 119
- Bill type: HR
- Bill number: 1527
- Origin chamber: House
- Introduced date: 2025-02-24
- Update date: 2026-02-04T05:06:17Z
- Update date including text: 2026-02-04T05:06:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-02-24: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-10 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2025-03-10 - Committee: Subcommittee Hearings Held
- 2025-04-09 - Committee: Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.
- 2025-04-09 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-02-24: Introduced in House

## Actions

- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-10 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2025-03-10 - Committee: Subcommittee Hearings Held
- 2025-04-09 - Committee: Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.
- 2025-04-09 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-24",
    "latestAction": {
      "actionDate": "2025-02-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1527",
    "number": "1527",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "J000307",
        "district": "10",
        "firstName": "John",
        "fullName": "Rep. James, John [R-MI-10]",
        "lastName": "James",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Reforming Education for Veterans Act",
    "type": "HR",
    "updateDate": "2026-02-04T05:06:17Z",
    "updateDateIncludingText": "2026-02-04T05:06:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-10",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-10",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-24",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-24",
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
          "date": "2025-02-24T17:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-04-09T21:01:58Z",
                "name": "Reported by"
              },
              {
                "date": "2025-04-09T20:53:56Z",
                "name": "Markup by"
              },
              {
                "date": "2025-03-10T19:16:15Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-03-10T19:16:09Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1527ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1527\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 24, 2025 Mr. James introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to make certain improvements to the laws administered by the Secretary of Veterans Affairs relating to educational assistance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reforming Education for Veterans Act .\n#### 2. Absence from certain education due to certain service\n##### (a) Options\nSection 3691A of title 38, United States Code, is amended by striking paragraph (1) of subsection (a) and inserting the following:\n(1) A covered member may, after receiving orders to enter a period of covered service\u2014 (A) withdraw from covered education; (B) take a leave of absence from covered education; or (C) subject to subsection (d), enter into an agreement with the institution concerned to complete a course of covered education to the satisfaction of such institution concerned. .\n##### (b) Conforming amendment\nSuch subsection is further amended, in paragraph (2)(A), by striking or takes a leave of absence and inserting , takes a leave of absence, or enters into an agreement .\n##### (c) Agreement\nSuch section is further amended by\u2014\n**(1)**\nredesignating subsection (d) as subsection (e); and\n**(2)**\nby inserting, after subsection (c), the following new subsection (d):\n(d) Agreement with institution concerned A covered member may enter into an agreement under subsection (a) only if the covered member has completed at least half of a course of covered education. .\n##### (d) Section heading\nSuch section is amended by striking the heading and inserting Absence from certain education due to certain service .\n##### (e) Table of sections\nThe table of sections at the beginning of chapter 36 of such title is amended by striking the item relating to section 3691A and inserting the following new item:\n3691A. Absence from certain education due to certain service. .\n#### 3. Department of Veterans Affairs compliance surveys\nSection 3693 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by adding at the end the following new paragraph:\n(3) In conducting annual compliance surveys under this subsection, the Secretary shall ensure that an educational institution or training establishment with multiple campuses is only required to complete one such survey if one school certifying official certifies veteran enrollment for all such campuses. ;\n**(2)**\nin subsection (c)\u2014\n**(A)**\nby striking not more than 10 business days of notice ;\n**(B)**\nby striking this section. and inserting this section\u2014 ; and\n**(C)**\nby adding at the end the following new paragraphs:\n(1) in the case of an educational institution or training establishment with a time stamp database collection feature, not more than 15 business days of notice; and (2) in the case of any other educational institution or training establishment, not more than 10 business days of notice. ; and\n**(3)**\nby striking subsection (d) and inserting the following:\n(d) Definitions In this section: (1) The terms educational institution and training establishment have the meanings given such terms in section 3452 of this title. (2) The term school certifying official means an employee of an educational institution with primary responsibility for certifying veteran enrollment at the educational institution. .\n#### 4. Notification of school certifying officials of handbook updates\n##### (a) In general\nNot later than 14 business days after updating the school certifying official handbook of the Department of Veterans Affairs, the Secretary of Veterans Affairs shall provide notice to all school certifying officials of such update.\n##### (b) School certifying official defined\nThe term school certifying official means an employee of an educational institution with primary responsibility for certifying veteran enrollment at the educational institution.",
      "versionDate": "2025-02-24",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Higher education",
            "updateDate": "2025-04-01T15:26:37Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2025-04-01T15:26:37Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-25T17:54:50Z"
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
      "date": "2025-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1527ih.xml"
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
      "title": "Reforming Education for Veterans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T13:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reforming Education for Veterans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T13:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to make certain improvements to the laws administered by the Secretary of Veterans Affairs relating to educational assistance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T13:03:50Z"
    }
  ]
}
```
