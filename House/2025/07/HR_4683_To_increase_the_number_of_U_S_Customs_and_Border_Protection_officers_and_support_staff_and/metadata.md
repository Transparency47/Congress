# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4683?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4683
- Title: Securing America’s Ports of Entry Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4683
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-05-16T08:07:40Z
- Update date including text: 2026-05-16T08:07:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-23 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-24 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-23 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-24 - Committee: Referred to the Subcommittee on Border Security and Enforcement.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4683",
    "number": "4683",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "K000402",
        "district": "26",
        "firstName": "Timothy",
        "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
        "lastName": "Kennedy",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Securing America\u2019s Ports of Entry Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:40Z",
    "updateDateIncludingText": "2026-05-16T08:07:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-24",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "text": "Referred to the Committee on Homeland Security, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Homeland Security, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:06:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-24T20:21:58Z",
              "name": "Referred to"
            }
          },
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-23T14:06:30Z",
          "name": "Referred To"
        }
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
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MS"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4683ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4683\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Kennedy of New York (for himself and Mr. Thompson of Mississippi ) introduced the following bill; which was referred to the Committee on Homeland Security , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo increase the number of U.S. Customs and Border Protection officers and support staff and to require reports that identify staffing, infrastructure, and equipment needed to enhance security at ports of entry.\n#### 1. Short title\nThis Act may be cited as the Securing America\u2019s Ports of Entry Act of 2025 .\n#### 2. Additional U.S. Customs and Border Protection personnel\n##### (a) Officers\nSubject to appropriations, the Commissioner for U.S. Customs and Border Protection shall hire, train, and assign not fewer than 1,000 new U.S. Customs and Border Protection officers above the current attrition level during every fiscal year until the total number of U.S. Customs and Border Protection officers equals and sustains the requirements identified each year in the Workload Staffing Model.\n##### (b) Support staff\nThe Commissioner is authorized to hire, train, and assign support staff, including technicians and Enterprise Services mission support, to perform non-law enforcement administrative functions to support the new U.S. Customs and Border Protection officers hired pursuant to subsection (a).\n##### (c) Traffic forecasts\nIn calculating the number of U.S. Customs and Border Protection officers needed at each port of entry through the Workload Staffing Model, the Commissioner shall\u2014\n**(1)**\nrely on data collected regarding the inspections and other activities conducted at each such port of entry;\n**(2)**\nconsider volume from seasonal surges, other projected changes in commercial and passenger volumes, the most current commercial forecasts, and other relevant information;\n**(3)**\nconsider historical volume and forecasts prior to the COVID\u201319 pandemic and the impact on international travel; and\n**(4)**\nincorporate personnel requirements for increasing the rate of outbound inspection operations at land ports of entry.\n##### (d) GAO report\nIf the Commissioner does not hire not fewer than 1,000 additional U.S. Customs and Border Protection officers authorized under subsection (a) during fiscal year 2026, or during any subsequent fiscal year in which the hiring requirements set forth in the Workload Staffing Model have not been achieved, the Comptroller General of the United States shall\u2014\n**(1)**\nconduct a review of U.S. Customs and Border Protection hiring practices to determine the reasons that such requirements were not achieved and other issues related to hiring by U.S. Customs and Border Protection; and\n**(2)**\nsubmit a report to the Committee on Homeland Security and Governmental Affairs of the Senate , the Committee on Finance of the Senate , the Committee on Homeland Security of the House of Representatives , and the Committee on Ways and Means of the House of Representatives that describes the results of the review conducted pursuant to paragraph (1).\n#### 3. Ports of entry infrastructure enhancement report\nNot later than 90 days after the date of the enactment of this Act, the Commissioner for U.S. Customs and Border Protection shall submit a report to the Committee on Homeland Security and Governmental Affairs of the Senate , the Committee on Finance of the Senate , the Committee on Homeland Security of the House of Representatives , and the Committee on Ways and Means of the House of Representatives that identifies\u2014\n**(1)**\ninfrastructure improvements at ports of entry that would enhance the ability of U.S. Customs and Border Protection officers to interdict opioids and other drugs that are being illegally transported into the United States, including a description of circumstances at specific ports of entry that prevent the deployment of technology used at other ports of entry;\n**(2)**\ndetection equipment that would improve the ability of such officers to identify opioids, including precursors and derivatives, that are being illegally transported into the United States; and\n**(3)**\nsafety equipment that would protect such officers from accidental exposure to such drugs or other dangers associated with the inspection of potential drug traffickers.\n#### 4. Reporting requirements\n##### (a) Temporary duty assignments\n**(1) Defined term**\nIn this subsection, the term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate ;\n**(B)**\nthe Committee on Appropriations of the Senate ;\n**(C)**\nthe Committee on Finance of the Senate ;\n**(D)**\nthe Committee on Homeland Security of the House of Representatives ;\n**(E)**\nthe Committee on Appropriations of the House of Representatives ; and\n**(F)**\nthe Committee on Ways and Means of the House of Representatives .\n**(2) Quarterly report**\nThe Commissioner for U.S. Customs and Border Protection shall submit a quarterly report to the appropriate congressional committees that includes, with respect to the reporting period\u2014\n**(A)**\nthe number of temporary duty assignments;\n**(B)**\nthe number of U.S. Customs and Border Protection officers required for each temporary duty assignment;\n**(C)**\nthe ports of entry from which such officers were reassigned;\n**(D)**\nthe ports of entry to which such officers were reassigned;\n**(E)**\nthe ports of entry at which reimbursable service agreements have been entered into that may be affected by temporary duty assignments;\n**(F)**\nthe duration of each temporary duty assignment;\n**(G)**\nthe cost of each temporary duty assignment; and\n**(H)**\nthe extent to which the temporary duty assignments within the reporting period were in support of the other U.S. Customs and Border Protection activities or operations along the southern border of the United States, including the specific costs associated with such temporary duty assignments.\n**(3) Notice**\nNot later than 10 days before redeploying employees from 1 port of entry to another, absent emergency circumstances\u2014\n**(A)**\nthe Commissioner shall notify the director of the port of entry from which employees will be reassigned of the intended redeployments; and\n**(B)**\nthe port director shall notify impacted facilities (including airports, seaports, and land ports) of the intended redeployments.\n**(4) Staff briefing**\nThe Commissioner shall brief all affected U.S. Customs and Border Protection employees regarding plans to mitigate vulnerabilities created by any planned staffing reductions at ports of entry.\n##### (b) Reports on U.S. Customs and Border Protection agreements\nSection 907(a) of the Trade Facilitation and Trade Enforcement Act of 2015 ( 19 U.S.C. 4451(a) ) is amended\u2014\n**(1)**\nin paragraph (3), by striking and an assessment and all that follows and inserting a period;\n**(2)**\nby redesignating paragraphs (4) through (12) as paragraphs (5) through (13), respectively;\n**(3)**\nby inserting after paragraph (3) the following:\n(4) A description of the factors that were considered before entering into the agreement, including an assessment of how the agreement provides economic benefits and security benefits (if applicable) at the port of entry to which the agreement relates. ; and\n**(4)**\nin paragraph (5), as redesignated, by inserting , including the locations of such services and the total hours of reimbursable services under the agreement, if any after the report .\n##### (c) Annual workload staffing model report\nAs part of the Annual Report on Staffing required under section 411(g)(5)(A) of the Homeland Security Act of 2002 ( 6 U.S.C. 211(g)(5)(A) ), the Commissioner for U.S. Customs and Border Protection shall include\u2014\n**(1)**\ninformation concerning the progress made toward meeting the U.S. Customs and Border Protection officer and support staff hiring targets set forth in section 2, while accounting for attrition;\n**(2)**\nan update to the information provided in the Resource Optimization at the Ports of Entry report, which was submitted to Congress on September 12, 2017, pursuant to the Department of Homeland Security Appropriations Act, 2017 (division F of Public Law 115\u201331 ); and\n**(3)**\na summary of the information included in the reports required under subsection (a) and section 907(a) of the Trade Facilitation and Trade Enforcement Act of 2015, as amended by subsection (b).",
      "versionDate": "2025-07-23",
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
        "actionDate": "2025-05-08",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "1678",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Securing America's Ports of Entry Act of 2025",
      "type": "S"
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
        "name": "Immigration",
        "updateDate": "2025-09-17T16:53:12Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4683ih.xml"
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
      "title": "Securing America\u2019s Ports of Entry Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-08T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Securing America\u2019s Ports of Entry Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To increase the number of U.S. Customs and Border Protection officers and support staff and to require reports that identify staffing, infrastructure, and equipment needed to enhance security at ports of entry.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:33:19Z"
    }
  ]
}
```
