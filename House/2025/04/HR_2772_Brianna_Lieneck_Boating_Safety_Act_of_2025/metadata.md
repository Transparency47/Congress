# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2772?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2772
- Title: Brianna Lieneck Boating Safety Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2772
- Origin chamber: House
- Introduced date: 2025-04-09
- Update date: 2025-09-11T08:06:13Z
- Update date including text: 2025-09-11T08:06:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-09 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- Latest action: 2025-04-09: Introduced in House

## Actions

- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-09 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2772",
    "number": "2772",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "G000597",
        "district": "2",
        "firstName": "Andrew",
        "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
        "lastName": "Garbarino",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Brianna Lieneck Boating Safety Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-11T08:06:13Z",
    "updateDateIncludingText": "2025-09-11T08:06:13Z"
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
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Coast Guard and Maritime Transportation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T16:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-09T20:52:34Z",
              "name": "Referred to"
            }
          },
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "NY"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2772ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2772\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2025 Mr. Garbarino (for himself and Mr. LaLota ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Secretary of the department in which the Coast Guard is operating to study and report to the Congress regarding recreational vessel operator training.\n#### 1. Short title\nThis Act may be cited as the Brianna Lieneck Boating Safety Act of 2025 .\n#### 2. Recreational vessel operator education and training\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Secretary of the department in which the Coast Guard is operating shall study and report to the Committee on Transportation and Infrastructure of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate regarding recreational vessel operator training. The study and report shall include a review of\u2014\n**(1)**\nCoast Guard Auxiliary and Power Squadron training programs;\n**(2)**\nexisting State boating education programs, including programs by the National Association of State Boating Law Administrators (in this section referred to as NASBLA ); and\n**(3)**\nother hands-on training programs available to recreational vessel operators.\n##### (b) Included subjects\nThe study shall specifically examine\u2014\n**(1)**\ncourse materials;\n**(2)**\ncourse content;\n**(3)**\ntraining methodology;\n**(4)**\nassessment methodology; and\n**(5)**\nrelevancy of course content to risks for recreational boaters.\n##### (c) Contents of report\nThe report under this section shall include\u2014\n**(1)**\na section regarding steps the Coast Guard and NASBLA have taken to encourage States to adopt mandatory recreational vessel operator training;\n**(2)**\nan evaluation of the ability of the States to harmonize their education programs and testing procedures;\n**(3)**\nan analysis of the extent States have provided reciprocity among the States for their respective mandatory and voluntary education requirements and programs;\n**(4)**\na section examining the level of uniformity of education and training between the States that currently have mandatory education and training programs;\n**(5)**\na section outlining the minimum standards for education of recreational vessel operators;\n**(6)**\na section analyzing how a Federal training and testing program can be harmonized with State training and testing programs;\n**(7)**\nan analysis of course content and delivery methodology for relevancy to risks for recreational boaters;\n**(8)**\na description of the current phase-in periods for mandatory boater education in State mandatory education programs and recommendation for the phase-in period for a mandatory boater education program including an evaluation as to whether the phase-in period affects course availability and cost;\n**(9)**\na description of the extent States allow for experienced boaters to bypass mandatory education courses and go directly to testing;\n**(10)**\nrecommendations for a bypass option for experienced boaters;\n**(11)**\na section analyzing how the Coast Guard would administer a Federal boating education, training, and testing program; and\n**(12)**\nan analysis of the extent to which a Federal boating education, training, and testing program should be required for all waters of a State, including internal waters.",
      "versionDate": "2025-04-09",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-28T14:17:14Z"
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
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2772ih.xml"
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
      "title": "Brianna Lieneck Boating Safety Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-23T11:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Brianna Lieneck Boating Safety Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-23T11:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of the department in which the Coast Guard is operating to study and report to the Congress regarding recreational vessel operator training.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-23T11:18:22Z"
    }
  ]
}
```
