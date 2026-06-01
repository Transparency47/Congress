# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7009?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7009
- Title: Home Affordability for Guard and Reserve Act
- Congress: 119
- Bill type: HR
- Bill number: 7009
- Origin chamber: House
- Introduced date: 2026-01-12
- Update date: 2026-04-09T18:47:52Z
- Update date including text: 2026-04-09T18:47:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-12: Introduced in House
- 2026-01-12 - IntroReferral: Introduced in House
- 2026-01-12 - IntroReferral: Introduced in House
- 2026-01-12 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-02-04 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2026-01-12: Introduced in House

## Actions

- 2026-01-12 - IntroReferral: Introduced in House
- 2026-01-12 - IntroReferral: Introduced in House
- 2026-01-12 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-02-04 - Committee: Referred to the Subcommittee on Economic Opportunity.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-12",
    "latestAction": {
      "actionDate": "2026-01-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7009",
    "number": "7009",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
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
    "title": "Home Affordability for Guard and Reserve Act",
    "type": "HR",
    "updateDate": "2026-04-09T18:47:52Z",
    "updateDateIncludingText": "2026-04-09T18:47:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-04",
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
      "actionDate": "2026-01-12",
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
      "actionDate": "2026-01-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-12",
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
          "date": "2026-01-12T17:03:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-04T19:42:15Z",
              "name": "Referred to"
            }
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7009ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7009\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 12, 2026 Mr. Barrett introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to expand eligibility for housing loans guaranteed by the Secretary of Veterans Affairs to members of the reserve components and the National Guard who perform certain duties, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Home Affordability for Guard and Reserve Act .\n#### 2. Eligibility of certain members of the reserve components and the National Guard for guaranteed housing loans\n##### (a) Expanded definition of active duty for purposes of housing loans\nSection 3701(b) of title 38, United States Code, is amended by adding at the end the following new paragraph:\n(9) The term active duty has the meanings as follows: (A) In the case of members of the regular components of the Armed Forces, the meaning given such term in section 101(21)(A). (B) In the case of members of the reserve components of the Armed Forces\u2014 (i) service on active duty (as defined in section 101(d) of title 10), inactive-duty training (as defined in section 101(d) of title 10), or annual training duty; or (ii) service on active duty under a call or order to active duty under section 688, 12301(a), 12301(d), 12301(g), 12301(h), 12302, 12304, 12304a, or 12304b of title 10 or section 713 of title 14, but not including inactive duty training (as defined in section 101(d) of title 10) or annual training duty. (C) In the case of a member of the Army National Guard of the United States or Air National Guard of the United States, in addition to service described in subparagraph (B), full-time service\u2014 (i) in the National Guard of a State for the purpose of organizing, administering, recruiting, instructing, or training the National Guard; (ii) in the National Guard when performing full-time National Guard duty (as defined in section 101 of title 32); or (iii) in the National Guard when performing active duty (as defined in section 101 of title 32). .\n##### (b) Retroactive applicability to service performed\nThe amendments made by this section shall apply with respect to any service performed on or after September 11, 2001.\n#### 3. Expansion of eligibility for guaranteed housing loans to certain additional personnel upon payment of additional loan fee\n##### (a) Expansion to individuals with at least 14 days of service\nSection 3701(b) of title 38, United States Code, is amended by inserting after paragraph (7) the following new paragraph:\n(8) The term veteran also includes, for purposes of home loans (subject to the additional loan fee in section 3729(b)(4)(J) of this title), an individual who\u2014 (A) is not otherwise eligible for the benefits of this chapter; (B) has completed a total service of at least 14 days on active duty under paragraph (B) or (C) of paragraph (9); and (C) following completion of such service, continued to serve until the completion of entry level and skill training (as defined in section 3301(3) of this title). .\n##### (b) Basic entitlement\nSection 3702(a)(2) of title 38, United States Code, is amended by adding at the end the following:\n(H) Each individual described in section 3701(b)(8) of this title. .\n##### (c) Additional loan fee for such individuals\nSection 3729(b)(4) of title 38, United States Code, is amended by adding at the end the following new subparagraph:\n(J) In the case of a housing loan in which the veteran has eligibility under section 3701(b)(8) of this title and does not otherwise have eligibility, the loan fee table in paragraph (2) shall be applied to the veteran or other obligor (as applicable) by adding 1.00 to the percentage in the table. .\n##### (d) Notification to personnel\nThe Secretary of Veterans Affairs shall ensure that each member of a reserve component or a member of the Army National Guard of the United States or Air National Guard of the United States who completes entry level and skill training (as defined in section 3301(3) of title 38, United States Code) after the date of the enactment of this Act is notified of their eligibility for housing loan benefits under chapter 37 of such title, including eligibility (subject to the additional loan fee) under section 3701(b)(8) of such title.",
      "versionDate": "2026-01-12",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-04-02",
        "text": "Placed on the Union Calendar, Calendar No. 497."
      },
      "number": "6047",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Sharri Briley and Eric Edmundson Veterans Benefits Expansion Act of 2026",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2026-02-10T23:23:48Z"
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
      "date": "2026-01-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7009ih.xml"
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
      "title": "Home Affordability for Guard and Reserve Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-02T22:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Home Affordability for Guard and Reserve Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-02T22:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to expand eligibility for housing loans guaranteed by the Secretary of Veterans Affairs to members of the reserve components and the National Guard who perform certain duties, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-02T22:03:21Z"
    }
  ]
}
```
