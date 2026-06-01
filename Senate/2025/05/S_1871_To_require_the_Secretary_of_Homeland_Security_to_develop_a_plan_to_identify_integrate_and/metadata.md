# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1871?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1871
- Title: Emerging Innovative Border Technologies Act
- Congress: 119
- Bill type: S
- Bill number: 1871
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2025-06-13T17:43:41Z
- Update date including text: 2025-06-13T17:43:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1871",
    "number": "1871",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Emerging Innovative Border Technologies Act",
    "type": "S",
    "updateDate": "2025-06-13T17:43:41Z",
    "updateDateIncludingText": "2025-06-13T17:43:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-05-22T16:51:19Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1871is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1871\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Ms. Cortez Masto (for herself and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require the Secretary of Homeland Security to develop a plan to identify, integrate, and deploy new, innovative, disruptive, or other emerging or advanced technologies that are safe and secure to enhance U.S. Customs and Border Protection's capabilities to meet its mission needs along international borders and at ports of entry.\n#### 1. Short title\nThis Act may be cited as the Emerging Innovative Border Technologies Act .\n#### 2. Innovative and emerging border technology plan\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Homeland Security, acting through the Commissioner for U.S. Customs and Border Protection (referred to in this section as CBP ) and the Under Secretary for Science and Technology of the Department of Homeland Security, and in consultation with the Department of Homeland Security's Chief Information Officer, Chief Procurement Officer, Privacy Officer, Officer for Civil Rights and Civil Liberties, and General Counsel, and any other relevant offices and components of the Department of Homeland Security, shall submit a plan to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Homeland Security of the House of Representatives for identifying, integrating, and deploying new, innovative, disruptive, or other emerging or advanced technologies that are safe and secure to enhance CBP capabilities to meet its mission needs along international borders or at ports of entry.\n##### (b) Contents\nThe plan required under subsection (a) shall include\u2014\n**(1)**\ninformation regarding how CBP utilizes the CBP Innovation Team authority under subsection (c) and other mechanisms to carry out the purposes described in subsection (a);\n**(2)**\nan assessment of the contributions directly attributable to such utilization;\n**(3)**\ninformation regarding\u2014\n**(A)**\nthe composition of each CBP Innovation Team; and\n**(B)**\nhow each CBP Innovation Team coordinates and integrates efforts with the CBP acquisition program office and other partners within CBP and the Department of Homeland Security;\n**(4)**\nthe identification of technologies used by other Federal departments or agencies not in use by CBP that could assist in enhancing mission needs along international borders or at ports of entry;\n**(5)**\nan analysis of authorities available to CBP to procure technologies referred to in subsection (a);\n**(6)**\nan assessment of whether additional or alternative authorities are needed to carry out the purposes described in subsection (a);\n**(7)**\nan explanation of how CBP plans to scale existing programs related to emerging or advanced technologies that are safe and secure into programs of record;\n**(8)**\na description of each planned security-related technology program, including objectives, goals, and timelines for each such program;\n**(9)**\nan assessment of the potential privacy, civil rights, civil liberties, and safety impacts of these technologies on individuals, and potential mitigation measures;\n**(10)**\nan assessment of CBP legacy border technology programs that could be phased out and replaced with technologies referred to in subsection (a), including cost estimates relating to such phase out and replacement;\n**(11)**\ninformation relating to how CBP is coordinating with the Department of Homeland Security\u2019s Science and Technology Directorate\u2014\n**(A)**\nto research and develop new, innovative, disruptive, or other emerging or advanced technologies that are safe and secure to carry out the purposes described in subsection (a);\n**(B)**\nto identify new, innovative, disruptive, or other emerging or advanced technologies that are safe and secure and that are in development or have been deployed by the private and public sectors and may satisfy the mission needs of CBP, with or without adaptation;\n**(C)**\nto incentivize the private sector to develop technologies, including privacy enhancing technologies, that may help CBP meet mission needs to enhance, or address capability gaps in, border security operations; and\n**(D)**\nto identify and assess ways to increase opportunities for communication and collaboration with the private sector, small, and disadvantaged businesses, intra-governmental entities, university centers of excellence, and Federal laboratories to leverage emerging technology and research within the public and private sectors;\n**(12)**\ninformation relating to how CBP is coordinating with the Department of Homeland Security official responsible for artificial intelligence policy to ensure the plan complies with the Department\u2019s policies and measures promoting responsible use of artificial intelligence;\n**(13)**\ninformation regarding metrics and key performance parameters for evaluating the effectiveness of efforts to identify, integrate, and deploy new, innovative, disruptive, or other emerging or advanced technologies that are safe and secure to carry out the purposes described in subsection (a);\n**(14)**\nthe identification of recent technological advancements relating to\u2014\n**(A)**\nmanned aircraft sensor, communication, and common operating picture technology;\n**(B)**\nunmanned aerial systems and related technology, including counter-unmanned aerial system technology;\n**(C)**\nsurveillance technology, including\u2014\n**(i)**\nmobile surveillance vehicles;\n**(ii)**\nassociated electronics, including cameras, sensor technology, and radar;\n**(iii)**\ntower-based surveillance technology;\n**(iv)**\nadvanced unattended surveillance sensors; and\n**(v)**\ndeployable, lighter-than-air, ground surveillance equipment;\n**(D)**\nnonintrusive inspection technology, including non-X-ray devices utilizing muon tomography and other advanced detection technology;\n**(E)**\ntunnel detection technology; and\n**(F)**\ncommunications equipment, including\u2014\n**(i)**\nradios;\n**(ii)**\nlong-term evolution broadband; and\n**(iii)**\nminiature satellites;\n**(15)**\ninformation relating to how CBP is coordinating with the Department of Homeland Security\u2019s Chief Information Officer, Chief Technology Officer, Privacy Officer, Civil Rights and Civil Liberties Officer, General Counsel, and other relevant offices and components of the Department in researching, developing, acquiring, or scaling new, innovative, disruptive, or other emerging or advanced technologies that are safe and secure; and\n**(16)**\nany other information the Secretary determines to be relevant.\n##### (c) CBP Innovation Team authority\n**(1) In general**\nThe Commissioner for CBP is authorized to maintain 1 or more CBP Innovation Teams to research and adapt commercial technologies that are new, innovative, disruptive, privacy enhancing, or otherwise emerging or advanced and may be used by CBP\u2014\n**(A)**\nto enhance mission needs along international borders and at ports of entry; and\n**(B)**\nto assess potential outcomes, including any negative consequences, of the introduction of emerging or advanced technologies with respect to which documented capability gaps in border security operations are yet to be determined.\n**(2) Functions**\nEach CBP Innovation Team shall\u2014\n**(A)**\noperate consistent with the Department of Homeland Security\u2019s and CBP's\u2014\n**(i)**\nprocurement and acquisition management policy; and\n**(ii)**\npolicies pertaining to responsible use of artificial intelligence; and\n**(B)**\nconsult with the Officer for Civil Rights and Civil Liberties and the Privacy Officer of the Department of Homeland Security to ensure programs, policies, and procedures involving civil rights, civil liberties, and privacy considerations are addressed in an integrated and comprehensive manner.\n**(3) Operating procedures, planning, strategic goals**\nThe Commissioner for CBP shall require each CBP Innovation Team maintained pursuant to paragraph (1) to establish, in coordination with other appropriate offices of the Department of Homeland Security\u2014\n**(A)**\noperating procedures, which shall include\u2014\n**(i)**\nspecificity regarding roles and responsibilities within each such team and with respect to Department of Homeland Security and non-Federal partners; and\n**(ii)**\nprotocols for entering into agreements to rapidly transition such technologies to existing or new programs of record to carry out the purposes described in subsection (a);\n**(B)**\nplanning and strategic goals for each such team that includes projected costs, time frames, metrics, and key performance parameters relating to the achievement of identified strategic goals, including a metric to measure the rate at which technologies described in subsection (a) are transitioned to existing or new programs of record in accordance with subparagraph (A); and\n**(C)**\noperating procedures that ensure each such team is in compliance with all applicable laws, rules, and regulations and with the Department of Homeland Security\u2019s policies pertaining to procurement and acquisition management, privacy, civil rights and civil liberties, and the responsible use of artificial intelligence, including risk assessments and ongoing monitoring to ensure accuracy and reliability.\n**(4) Annual report**\nNot later than 180 days after the date of the enactment of this Act and annually thereafter, the Commissioner for CBP shall submit to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Homeland Security of the House of Representatives information relating to the activities of the CBP Innovation Teams, including\u2014\n**(A)**\ncopies of operating procedures and protocols required under paragraph (3)(A) and planning and strategic goals required under paragraph (3)(B);\n**(B)**\ndescriptions of the technologies piloted by each such team during the immediately preceding fiscal year, including\u2014\n**(i)**\ninformation regarding which such technologies are determined to have been successful; and\n**(ii)**\nthe identification of documented capability gaps that are being addressed; and\n**(C)**\ninformation regarding the status of efforts to rapidly transition technologies determined successful to existing or new programs of record.\n##### (d) Cost-Benefit\nBefore initiating the large-scale deployment of any new technology contained in the plan required under subsection (a), the Secretary of Homeland Security shall consider the costs and benefits to the Federal Government to ensure that the deployment of such technology will provide quantifiable improvements to border security.",
      "versionDate": "2025-05-22",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-06-13T17:43:41Z"
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
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1871is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Emerging Innovative Border Technologies Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-04T03:23:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Emerging Innovative Border Technologies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Homeland Security to develop a plan to identify, integrate, and deploy new, innovative, disruptive, or other emerging or advanced technologies that are safe and secure to enhance U.S. Customs and Border Protection's capabilities to meet its mission needs along international borders and at ports of entry.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:45Z"
    }
  ]
}
```
