# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5231?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5231
- Title: Safe Airspace for Americans Act
- Congress: 119
- Bill type: HR
- Bill number: 5231
- Origin chamber: House
- Introduced date: 2025-09-09
- Update date: 2025-10-07T08:05:23Z
- Update date including text: 2025-10-07T08:05:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-09: Introduced in House
- 2025-09-09 - IntroReferral: Introduced in House
- 2025-09-09 - IntroReferral: Introduced in House
- 2025-09-09 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-09 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-10 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-09-09: Introduced in House

## Actions

- 2025-09-09 - IntroReferral: Introduced in House
- 2025-09-09 - IntroReferral: Introduced in House
- 2025-09-09 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-09 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-10 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-09",
    "latestAction": {
      "actionDate": "2025-09-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5231",
    "number": "5231",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "G000598",
        "district": "42",
        "firstName": "Robert",
        "fullName": "Rep. Garcia, Robert [D-CA-42]",
        "lastName": "Garcia",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Safe Airspace for Americans Act",
    "type": "HR",
    "updateDate": "2025-10-07T08:05:23Z",
    "updateDateIncludingText": "2025-10-07T08:05:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-09",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-09",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-09",
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
          "date": "2025-09-09T14:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-09-10T21:43:07Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-09-09T14:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "WI"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "FL"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "TN"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-09-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5231ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5231\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 9, 2025 Mr. Garcia of California (for himself, Mr. Grothman , Mr. Moskowitz , and Mr. Ogles ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Administrator of the Federal Aviation Administration to establish procedures and reporting requirements for incidents relating to unidentified anomalous phenomena, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safe Airspace for Americans Act .\n#### 2. Unidentified anomalous phenomena\n##### (a) In general\nNot later than 180 days after the enactment of this Act, the Administrator of the Federal Aviation Administration shall\u2014\n**(1)**\ndevelop procedures to synchronize and standardize the collection, reporting, and analysis of incidents, including adverse physiological effects, or the disruption, interference, or interaction with flight instruments, potentially caused by an unidentified anomalous phenomena reported by civilian aircrew, air traffic controllers, flight attendants, aviation maintenance personnel, aviation dispatchers, air carriers or operators, and airports;\n**(2)**\ndevelop processes and procedures to ensure that such incidents are reported and stored in an appropriate manner that allows for the integration of analysis of such information;\n**(3)**\nestablish procedures to provide employees of the Federal Aviation Administration the ability for timely and consistent reporting of such incidents that could reasonably be considered an unidentified anomalous phenomena;\n**(4)**\ndevelop processes and procedures to ensure the timely investigations of such incidents, including immediately archiving information or data, including pilot-controller communications as well as air traffic management system and radar data, that could be used to aid in such investigations; and\n**(5)**\nevaluate the threat that such incidents present to the safety of the national airspace system.\n##### (b) Coordination\nIn carrying out the requirements of this section, the Administrator shall coordinate with the heads of other departments and agencies of the Federal Government, as appropriate, including the Secretary of Defense, the Director of National Intelligence, the Administrator of the National Aeronautics and Space Administration, the Secretary of Homeland Security, the Administrator of the National Oceanic and Atmospheric Administration, the Director of the National Science Foundation, and the Secretary of Energy.\n##### (c) All-Domain Anomaly Resolution Office\nThe Administrator shall share the reports and all incident archived information and data submitted under this section with the All-Domain Anomaly Resolution Office of the Department of Defense.\n##### (d) Prohibition against use of reports for enforcement purposes\nThe Administrator may not use reports submitted under this section (or information derived therefrom) in any enforcement action except information concerning accidents or criminal offenses.\n##### (e) Communications strategy\nNot later than 180 days after the date of enactment of this Act, the Administrator shall produce and implement a communications strategy to\u2014\n**(1)**\nengage the public and publicize the reporting process described under subsection (a); and\n**(2)**\ndecrease stigma towards individuals submitting information to the Administrator under this section.\n##### (f) Reporting system\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Administrator shall select whether reports submitted under this section shall be received through\u2014\n**(A)**\nthe Aviation Safety Reporting Program in effect as of the date of enactment of this Act; or\n**(B)**\na new and separate system similar to such Program that is established to exclusively receive report of potential unidentified anomalous phenomena.\n**(2) Consideration**\nIf the Administrator makes a selection under paragraph (1)(A), not later than 1 year after the date of enactment of this Act, the Administrator shall consider whether to update the Aviation Safety Reporting Program reporting intake system to improve the capture information regarding whether a reported event could involve an unidentified anomalous phenomenon, and, if so, a mechanism for including description of the object subject to such report and the apparent kinematics of such object.\n**(3) System requirement**\nIf the Administrator makes a selection under paragraph (1)(B), the Administrator shall ensure the system includes the ability to provide a description of the object subject to such report and the apparent kinematics of such object.\n**(4) Manner of submission**\nThe Administrator shall include in the reporting system selected under this subsection the ability to submit such a report via an electronic flight bag if the Administrator determines that submitting via such flight bag can be done\u2014\n**(A)**\nsafely; and\n**(B)**\nwithout compromising pilots\u2019 ability to aviate, navigate and communicate.\n##### (g) Protection of medical certificates\nThe spotting, visual witness, or reporting of unidentified anomalous phenomena shall not be taken into account for the purposes of evaluation of mental standards for issuing medical certificates for airmen and for remaining eligible for a medical certificate under part 67 of title 14, Code of Federal Regulations.\n##### (h) Protection of airmen certificates\nThe spotting, visual witness, or reporting of unidentified anomalous phenomena may not be taken into account for the purposes of evaluation of competency for issuing airmen certificates under section 44709 of title 49, United States Code.\n##### (i) Prohibition on reprisals for Federal employees and contractors\nAn employee of a department or agency of the Federal Government, or of a contractor, subcontractor, grantee, subgrantee, or personal services contractor of such a department or agency, who has authority to take, direct others to take, recommend, or approve any personnel action, shall not, with respect to such authority, take or fail to take, or threaten to take or fail to take, a personnel action, including the revocation or suspension of security clearances, or termination of employment, with respect to any individual as a reprisal for spotting, visually witnessing or reporting of unidentified anomalous phenomena.\n##### (j) Prohibition on reprisals for employees of air carriers or commercial operators\nAn air carrier or commercial operator under part 119 of title 14, Code of Federal Regulations shall not\u2014\n**(1)**\ntake or fail to take, or threaten to take or fail to take, a personnel action, or termination of employment, with respect to any individual as a reprisal for spotting, visually witnessing or reporting of unidentified anomalous phenomena to the Administrator; or\n**(2)**\nissue a cease and desist letter to any individual or organization for spotting, visually witnessing, or reporting of unidentified anomalous phenomena to the Administrator.\n##### (k) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nall unidentified anomalous phenomena encounters by aviation personnel should be reported, particularly when such encounters involve a potential safety or national security concern; and\n**(2)**\nemployers and governmental officials should take actions to reduce the stigma of reporting unidentified anomalous phenomena.\n##### (l) Definitions\nIn this Act:\n**(1) Unidentified anomalous phenomena**\nThe term unidentified anomalous phenomena means\u2014\n**(A)**\nan airborne object that is not immediately identifiable;\n**(B)**\na transmedium object or device; and\n**(C)**\na submerged object or device that\u2014\n**(i)**\nis not immediately identifiable; and\n**(ii)**\ndisplays behavior or performance characteristics suggesting that the object or device may be related to an object described in subparagraph (A).\n**(2) Transmedium object or device**\nThe term transmedium object or device means an object or device that is\u2014\n**(A)**\nobserved to transition between space and the atmosphere, or between the atmosphere and a body of water; and\n**(B)**\nnot immediately identifiable.",
      "versionDate": "2025-09-09",
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
        "updateDate": "2025-09-23T18:50:33Z"
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
      "date": "2025-09-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5231ih.xml"
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
      "title": "Safe Airspace for Americans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-16T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safe Airspace for Americans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-16T04:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Administrator of the Federal Aviation Administration to establish procedures and reporting requirements for incidents relating to unidentified anomalous phenomena, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-16T04:48:16Z"
    }
  ]
}
```
