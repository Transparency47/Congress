# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3334?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3334
- Title: USCP Empowerment Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3334
- Origin chamber: House
- Introduced date: 2025-05-13
- Update date: 2026-02-03T09:05:42Z
- Update date including text: 2026-02-03T09:05:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-13: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committees on Transportation and Infrastructure, and the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-13 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committees on Transportation and Infrastructure, and the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-13 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committees on Transportation and Infrastructure, and the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-02 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-05-13: Introduced in House

## Actions

- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committees on Transportation and Infrastructure, and the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-13 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committees on Transportation and Infrastructure, and the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-13 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committees on Transportation and Infrastructure, and the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-02 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-13",
    "latestAction": {
      "actionDate": "2025-05-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3334",
    "number": "3334",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001132",
        "district": "2",
        "firstName": "Elijah",
        "fullName": "Rep. Crane, Elijah [R-AZ-2]",
        "lastName": "Crane",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "USCP Empowerment Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-03T09:05:42Z",
    "updateDateIncludingText": "2026-02-03T09:05:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
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
      "actionDate": "2025-05-13",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committees on Transportation and Infrastructure, and the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-13",
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
      "text": "Referred to the Committee on House Administration, and in addition to the Committees on Transportation and Infrastructure, and the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-13",
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
      "text": "Referred to the Committee on House Administration, and in addition to the Committees on Transportation and Infrastructure, and the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-13",
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
          "date": "2025-05-13T16:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:24:59Z",
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
          "date": "2025-05-13T16:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-13T16:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "PA"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "AL"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3334ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3334\nIN THE HOUSE OF REPRESENTATIVES\nMay 13, 2025 Mr. Crane (for himself, Mr. Perry , and Mr. Moore of Alabama ) introduced the following bill; which was referred to the Committee on House Administration , and in addition to the Committees on Transportation and Infrastructure , and the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo authorize the United States Capitol Police to take action with respect to threats from unmanned aircraft systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the USCP Empowerment Act of 2025 .\n#### 2. Authority of United States Capitol Police with respect to unmanned aircraft and unmanned aircraft systems\n##### (a) Authority\nNotwithstanding section 46502 of title 49, United States Code, or sections 32, 1030, and 1367 and chapters 119 and 206 of title 18, United States Code, the Capitol Police Board may take, and may authorize personnel in the United States Capitol Police with assigned duties that include the security or protection of people, facilities, or assets to take, such actions as are described in subsection (b)(1) that are necessary to mitigate a credible threat, as defined by the Capitol Police Board, that an unmanned aircraft system poses to the safety or security of a covered Capitol Police facility or asset.\n##### (b) Actions described\n**(1) In general**\nThe actions authorized in subsection (a) are the following:\n**(A)**\nDuring the operation of the unmanned aircraft system, detect, identify, monitor, and track the unmanned aircraft system, without prior consent, including by means of intercept or other access of a wire communication, an oral communication, or an electronic communication used to control the unmanned aircraft system.\n**(B)**\nWarn the operator of the unmanned aircraft system, including by passive or active, and direct or indirect physical, electronic, radio, and electromagnetic means.\n**(C)**\nDisrupt control of the unmanned aircraft system, without prior consent, including by disabling the unmanned aircraft system by intercepting, interfering, or causing interference with wire, oral, electronic, or radio communications used to control the unmanned aircraft system.\n**(D)**\nSeize or exercise control of the unmanned aircraft system.\n**(E)**\nSeize or otherwise confiscate the unmanned aircraft system.\n**(F)**\nUse reasonable force, if necessary, to disable, damage, or destroy the unmanned aircraft system.\n**(2) Required coordination**\n**(A) In general**\nThe Capitol Police Board shall develop the actions described in paragraph (1) in coordination with the Secretary of Transportation.\n**(B) Federal Aviation Administration**\nThe Capitol Police Board shall coordinate with the Administrator of the Federal Aviation Administration when any action authorized by this section may affect aviation safety, civilian aviation or aerospace operations, aircraft worthiness, or the use of the airspace.\n**(3) Research, testing, training, and evaluation**\nThe Capitol Police Board may conduct research, testing, training on, or evaluation of any equipment, including any electronic equipment, to determine the capability or utility of the equipment prior to the use of the equipment or the technology included in the equipment for any action described in subsection (b)(1).\n##### (c) Forfeiture\nAny unmanned aircraft system described in subsection (a) seized pursuant to this section is subject to forfeiture to the United States.\n##### (d) Regulations and guidance\n**(1) In general**\nIn coordination with the Secretary of Transportation, the Capitol Police Board may prescribe regulations and shall issue guidance to carry out this Act.\n**(2) Federal Aviation Administration**\nThe Capitol Police Board shall coordinate with the Administrator of the Federal Aviation Administration to issue any guidance or otherwise implement this section if such guidance or implementation may affect aviation safety, civilian aviation or aerospace operations, aircraft airworthiness, or the use of airspace.\n##### (e) Privacy protection\nThe regulations or guidance issued to carry out the actions authorized under subsection (b) shall ensure that\u2014\n**(1)**\nthe interception or acquisition of, or access to, or maintenance or use of, communications to or from an unmanned aircraft system under this section is conducted in a manner consistent with the First and Fourth Amendments to the Constitution of the United States and applicable provisions of Federal law;\n**(2)**\ncommunications to or from an unmanned aircraft system are intercepted or acquired only to the extent necessary to support an action described in subsection (b)(1);\n**(3)**\nrecords of such communications are maintained only for as long as necessary, and in no event for more than 180 days, unless the Capitol Police Board determines that maintenance of such records is necessary to investigate or prosecute a violation of law, directly support an ongoing security operation, is required under Federal law, or for the purpose of any litigation;\n**(4)**\nsuch communications are not disclosed outside the United States Capitol Police unless the disclosure\u2014\n**(A)**\nis necessary to investigate or prosecute a violation of law;\n**(B)**\nwould support the Department of Defense, a Federal law enforcement agency, or the enforcement activities of a regulatory agency of the Federal Government in connection with a criminal or civil investigation of, or any regulatory, statutory, or other enforcement action relating to an action described in subsection (b)(1); or\n**(C)**\nis otherwise required by law; and\n**(5)**\nto the extent necessary, the United States Capitol Police may share threat information, which shall not include communications referred to in subsection (b), with State, local, territorial, or tribal law enforcement agencies in the course of a security or protection operation.\n##### (f) Report to Congress\n**(1) In general**\nNot later than 6 months after the date of the enactment of this section, and every 6 months thereafter, the Chief of the Capitol Police, or another individual designated by the Capitol Police Board, shall provide to the appropriate congressional committees a written report on the activities of the Capitol Police Board carried out under this section.\n**(2) Content**\nThe report described in paragraph (1) shall include\u2014\n**(A)**\npolicies, programs, and procedures to mitigate or eliminate impacts of such activities to the National Airspace System;\n**(B)**\na description of instances in which actions described in subsection (b)(1) have been taken, including all such instances that may have resulted in harm, damage, or loss to a person or to private property;\n**(C)**\na description of the guidance, policies, or procedures established to address privacy, civil rights, and civil liberties issues implicated by the actions allowed under this section, as well as any changes or subsequent efforts that would significantly affect privacy, civil rights or civil liberties;\n**(D)**\na description of options considered and steps taken to mitigate any identified impacts to the national airspace system related to the use of any system or technology, including the minimization of the use of any technology that disrupts the transmission of radio or electronic signals, for carrying out the actions described in subsection (b)(1);\n**(E)**\na description of instances in which communications intercepted or acquired during the course of operations of an unmanned aircraft system were held for more than 180 days or shared outside of the United States Capitol Police;\n**(F)**\nhow the Capitol Police Board has\u2014\n**(i)**\ninformed the public as to the possible use of authorities under this section; and\n**(ii)**\nengaged with Federal, State, and local law enforcement agencies to implement and use such authorities; and\n**(G)**\na description of any new technology or equipment deployed by the Capitol Police Board to carry out the actions described in subsection (b)(1) and the options considered to mitigate any identified impacts to the national airspace system related to the use of the technology or equipment.\n**(3) Unclassified form**\nThe report described in paragraph (1) shall be in unclassified form, but may be accompanied by an additional classified annex.\n##### (g) Rules of construction\n**(1)**\nNothing in this section may be construed to vest in the Capitol Police Board any authority of the Secretary of Transportation or the Administrator of the Federal Aviation Administration.\n**(2)**\nNothing in this section may be construed to vest in the Secretary of Transportation or the Administrator of the Federal Aviation Administration any authority of the Capitol Police Board.\n##### (h) Termination\nThe authority to carry out this section with respect to a covered Capitol Police facility or asset described in subparagraph (C) of subsection (j)(2) shall terminate on the date identified in section 210G(i) of the Homeland Security Act of 2002 ( 6 U.S.C. 124n ).\n##### (i) Scope of authority\nThe Capitol Police Board may not operate any other program to mitigate a credible threat posed by an unmanned aircraft system other than the program under this section.\n##### (j) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means the following:\n**(A)**\nThe Committee on House Administration of the House of Representatives.\n**(B)**\nThe Committee on Rules and Administration of the Senate.\n**(2) Covered Capitol Police facility or asset**\nThe term covered Capitol Police facility or asset means\u2014\n**(A)**\nthe Capitol Buildings as described in section 5101 of title 40, United States Code;\n**(B)**\nthe United States Capitol Grounds as described in section 5102 of title 40, United States Code; or\n**(C)**\nany area described in section 9A(a) of the Act entitled An Act to define the area of the United States Capitol Grounds, to regulate the use thereof, and for other purposes , approved July 31, 1946 ( 2 U.S.C. 1966(a) ), as directed by the Capitol Police Board.\n**(3) Electronic communication; intercept; oral communication; wire communication**\nThe terms electronic communication , intercept , oral communication , and wire communication have the meaning given those terms in section 2510 of title 18, United States Code.\n**(4) Unmanned aircraft system**\nThe term unmanned aircraft system has the meaning given such term in section 44801 of title 49, United States Code.",
      "versionDate": "2025-05-13",
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
        "updateDate": "2025-05-28T12:37:09Z"
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
      "date": "2025-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3334ih.xml"
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
      "title": "USCP Empowerment Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "USCP Empowerment Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the United States Capitol Police to take action with respect to threats from unmanned aircraft systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T04:48:27Z"
    }
  ]
}
```
