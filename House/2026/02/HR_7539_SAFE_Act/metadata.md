# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7539?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7539
- Title: SAFE Act
- Congress: 119
- Bill type: HR
- Bill number: 7539
- Origin chamber: House
- Introduced date: 2026-02-12
- Update date: 2026-04-28T08:05:44Z
- Update date including text: 2026-04-28T08:05:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-02-12: Introduced in House

## Actions

- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7539",
    "number": "7539",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "H001096",
        "district": "",
        "firstName": "Harriet",
        "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
        "lastName": "Hageman",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "SAFE Act",
    "type": "HR",
    "updateDate": "2026-04-28T08:05:44Z",
    "updateDateIncludingText": "2026-04-28T08:05:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-12",
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
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T14:06:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
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
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "OH"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "NJ"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "IL"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "IN"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "SD"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "TX"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7539ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7539\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2026 Ms. Hageman introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Administrator of the Federal Motor Carrier Safety Administration to conduct a study on chameleon carriers in the United States and plan, develop, and test an advanced automation tool to help enforcement personnel detect chameleon carrier applications under the registration process of the Department of Transportation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safety and Accountability in Freight Enforcement Act or the SAFE Act .\n#### 2. Report on chameleon carriers\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Comptroller General of the United States shall submit to Congress a report that contains the results of a study that examines chameleon carriers on United States roadways.\n##### (b) Contents\nThe report under subsection (a) shall include\u2014\n**(1)**\nthe estimated number of chameleon carriers on United States roadways at any given time;\n**(2)**\nthe prevalence of chameleon carriers on United States roadways since the issuance of the report of the Government Accountability Office titled Motor Carrier Safety: New Applicant Reviews Should Expand to Identify Freight Carriers Evading Detection , issued March 22, 2012;\n**(3)**\nthe estimated number of fatalities caused by chameleon carriers since the report described in paragraph (2), including the number of fatalities broken down by State;\n**(4)**\nthe estimated number of serious bodily injuries caused by chameleon carriers since the report described in paragraph (2), including the number of serious bodily injuries broken down by State;\n**(5)**\nthe estimated amount of property damage caused by chameleon carriers since the report described in paragraph (2);\n**(6)**\nan identification and analysis of the methods and techniques used by chameleon carriers to evade Federal enforcement, including how such methods and techniques have evolved over time;\n**(7)**\nan identification and analysis of the existing monitoring and enforcement capabilities, along with any shortcomings, of the Department of Transportation to detect and mitigate chameleon carrier activity, including\u2014\n**(A)**\nthe registration processes for Department of Transportation numbers;\n**(B)**\nthe existing software capabilities of the Department of Transportation to detect chameleon carrier applicants;\n**(C)**\nany recommendations for improving data fields within the Motor Carrier Management Information System; and\n**(D)**\nany existing penalties laid out under Federal statute and regulation for chameleon carriers;\n**(8)**\nany other relevant priorities deemed necessary by the Department of Transportation; and\n**(9)**\nany legislative recommendations to address chameleon carriers.\n##### (c) Collaboration\nIn carrying out the study under subsection (a), the Comptroller General may collaborate with other Federal agencies, State and local governments, institutions of higher education, and private sector entities.\n#### 3. Advanced automation tool\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Administrator of the Federal Motor Carrier Safety Administration shall develop, test, and implement an advanced automation tool to help Federal Motor Carrier Safety Administration registration personnel detect chameleon carrier applications under the registration process for Department of Transportation numbers.\n##### (b) Collaboration\n**(1) In general**\nIn developing the tool under subsection (a), the Administrator may collaborate with other Federal agencies, State and local governments, institutions of higher education, and the private sector as necessary to develop and test the advanced automation tool.\n**(2) Federal agencies**\nThe Administrator and any Federal agency the Administrator determines is relevant shall enter into a memorandum of understanding to share information needed to implement the requirements of the tool under subsection (c), which may include\u2014\n**(A)**\nthe Department of Treasury;\n**(B)**\nthe Department of Justice;\n**(C)**\nthe United States Postal Service;\n**(D)**\nthe Department of Homeland Security;\n**(E)**\nthe Department of Commerce;\n**(F)**\nthe Department of State; and\n**(G)**\nrelevant operating administrations within the Department of Transportation.\n**(3) State agencies**\nThe Administrator shall enter into a memorandum of understanding with any relevant State agency to share information needed to implement the requirements of the tool under subsection (c).\n##### (c) Requirements\nThe advanced automation tool developed under subsection (a) shall include\u2014\n**(1)**\nthe ability to detect chameleon carrier-like characteristics that support evidence of substantial continuity between entities, including\u2014\n**(A)**\nwhether the new or affiliated entity was created for the purpose of evading statutory or regulatory requirements, a Federal Motor Carrier Safety Administration order, enforcement action, or negative compliance history;\n**(B)**\nthe previous entity's safety performance history, including, among other things, safety violations and enforcement actions of the Secretary, if any;\n**(C)**\nexisting or inactive Department of Transportation numbers;\n**(D)**\nconsideration exchanged for assets purchased or transferred;\n**(E)**\ndates of company creation and dissolution or cessation of operations;\n**(F)**\ncommonality of ownership between the current and former company or between current companies;\n**(G)**\ncommonality of officers and management personnel;\n**(H)**\nidentity of physical or mailing addresses, telephone, fax numbers, or email addresses;\n**(I)**\nidentity of motor vehicle equipment;\n**(J)**\ncontinuity of liability insurance policies or commonality of coverage under such policies;\n**(K)**\ncommonality of drivers and other employees;\n**(L)**\ncontinuation of carrier facilities and other physical assets;\n**(M)**\ncontinuity or commonality of nature and scope of operations; and\n**(N)**\nadvertising, corporate name, or other acts through which the company holds itself out to the public;\n**(2)**\nthe ability to detect lapses in insurance coverage;\n**(3)**\nthe ability to compile evidence of the chameleon carrier-like characteristics under paragraph (1) relevant to the determination of a registration application for Department of Transportation numbers;\n**(4)**\nthe ability to provide automated decision support relevant to the determination of any registration application for Department of Transportation numbers, while keeping responsibility for final determinations on employees of the Administration;\n**(5)**\nthe ability to automate information sharing between Federal agencies; and\n**(6)**\nany other relevant priorities determined necessary by the Administrator.\n##### (d) Appeals for redetermination\n**(1) In general**\nIn establishing the tool under this section, the Administrator shall develop an appeals process under which persons denied a Department of Transportation number on the basis of a flag by such tool may seek a review of the denial.\n**(2) Notification**\nIn establishing the tool under this section, the Administrator shall provide for a process under which a person denied a Department of Transportation number as described in paragraph (1) shall receive a notification of such denial that includes the factors flagged by the tool and provides instructions to such person to correct the application for such number not later than 30 days after receipt of the notification.\n**(3) Timing of redetermination**\nThe appeals process developed under paragraph (1) shall provide for a redetermination on the amended application for a Department of Transportation number to take place not later than 30 days after the receipt of the information described in paragraph (2).\n##### (e) Briefing\nNot later than 30 days after the date of enactment of this Act, the Administrator shall brief the congressional committees of jurisdiction on the issue of chameleon carriers and any ongoing efforts or progress that the Administration has made to combat such issue or meet the objectives of this Act.\n##### (f) Rule of construction\nNothing in this Act shall be construed to allow the final use of an automated decision by the tool created under this section for Department of Transportation number registration.\n##### (g) Data privacy\nIn developing the tool under subsection (a), the Administrator shall ensure that data used by such tool is not disclosed for a purpose not described in this section.\n##### (h) Audit and report on effectiveness\n**(1) In general**\nNot later than 2 years after the date of implementation of the tool established under this section, the inspector general of the Department of Transportation shall submit to Congress a report on the effectiveness of such tool.\n**(2) Contents**\nThe report under paragraph (1) shall contain\u2014\n**(A)**\nthe results of an audit of the effectiveness of the tool established under this section;\n**(B)**\nempirical data on outcomes of the use of the tool, including the number of flagged and rejected applications for Department of Transportation numbers, any reduction in severe crashes, and the number of errors and application redeterminations under subsection (d); and\n**(C)**\nany recommendations to improve the effectiveness of the tool.\n#### 4. Definition of chameleon carrier\nIn this Act, the term chameleon carrier means a motor carrier, intermodal equipment provider, broker, or freight forwarder, or an officer, employee, agent, authorized representative, or other affiliated party of such an entity, that has, directly or indirectly, operated or attempted to operate a motor carrier, intermodal equipment provider, broker, or freight forwarder under a new identity or as an affiliated entity to\u2014\n**(1)**\navoid complying with a Federal Motor Carrier Safety Administration order;\n**(2)**\navoid complying with a statutory or regulatory requirement;\n**(3)**\navoid paying a civil penalty;\n**(4)**\navoid responding to an enforcement action;\n**(5)**\navoid being linked with a negative compliance history;\n**(6)**\navoid or evade increased insurance premiums, policy cancellations, or underwriting restrictions by obtaining or attempting to obtain insurance coverage under a new or materially different identity, ownership structure, or corporate form;\n**(7)**\nmisrepresent ownership, control, management, or operational continuity to an insurer, broker, or underwriter for the purpose of securing lower insurance rates or favorable coverage terms; or\n**(8)**\nreincorporate, re-register, or otherwise reconstitute a carrier entity following the denial, nonrenewal, or cancellation of an insurance policy due to safety, claims, or compliance history.",
      "versionDate": "2026-02-12",
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
        "updateDate": "2026-03-09T18:03:58Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7539ih.xml"
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
      "title": "SAFE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-07T04:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAFE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-07T04:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safety and Accountability in Freight Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-07T04:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Administrator of the Federal Motor Carrier Safety Administration to conduct a study on chameleon carriers in the United States and plan, develop, and test an advanced automation tool to help enforcement personnel detect chameleon carrier applications under the registration process of the Department of Transportation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-07T04:18:25Z"
    }
  ]
}
```
