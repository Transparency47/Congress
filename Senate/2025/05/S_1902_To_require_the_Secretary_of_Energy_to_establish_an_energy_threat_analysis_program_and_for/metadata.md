# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1902?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1902
- Title: ETAP Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1902
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1902",
    "number": "1902",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "R000584",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Risch, James E. [R-ID]",
        "lastName": "Risch",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "ETAP Act of 2025",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
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
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
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
          "date": "2025-05-22T19:08:12Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1902is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1902\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Risch (for himself and Mr. Hickenlooper ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo require the Secretary of Energy to establish an energy threat analysis program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Energy Threat Analysis Program Act of 2025 or the ETAP Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Department**\nThe term Department means the Department of Energy.\n**(2) Program**\nThe term Program means the energy threat analysis program established under section 3.\n**(3) Secretary**\nThe term Secretary means the Secretary of Energy.\n#### 3. Energy Threat Analysis Program\n##### (a) In general\nAs part of the program developed under section 40125(c) of the Infrastructure Investment and Jobs Act ( 42 U.S.C. 18724(c) ), the Secretary shall establish an energy threat analysis program\u2014\n**(1)**\nunder which the Office of Cybersecurity, Energy Security, and Emergency Response, in consultation with the Office of Intelligence and Counterintelligence, may establish, for activities of the program to advance public-private operational collaboration\u2014\n**(A)**\nan Energy Threat Analysis Center as a physical location; and\n**(B)**\nany other additional facilities, as necessary;\n**(2)**\nto enhance situational awareness of threats to the security of the energy sector;\n**(3)**\nto analyze threats against the security of the energy sector;\n**(4)**\nto identify relevant security threat mitigation measures for energy systems;\n**(5)**\nto support relevant response and restoration activities for the energy sector under existing constructs;\n**(6)**\nto inform research and development activities in support of the security of critical energy systems, technologies, and components;\n**(7)**\nto conduct other security and resilience efforts identified by the Secretary;\n**(8)**\nto enhance and periodically test the emergency response capabilities of the Department;\n**(9)**\nto expand cooperation of the Department with the intelligence community for energy sector-related threat collection and analysis;\n**(10)**\nto enhance the tools of the Department and the Electricity Information Sharing and Analysis Center for monitoring the status of the energy sector; and\n**(11)**\nto expand industry participation in the Electricity Information Sharing and Analysis Center.\n##### (b) Administration\nThe Program shall be\u2014\n**(1)**\ndirected by the Secretary;\n**(2)**\nmanaged by the Office of Cybersecurity, Energy Security, and Emergency Response; and\n**(3)**\nsupported by the Office of Intelligence and Counterintelligence.\n##### (c) Functions\nThe functions of the Program shall include\u2014\n**(1)**\nsupporting public-private operational collaboration for the government and industry\u2014\n**(A)**\nto develop actionable operational information relating to threats to the security of the energy sector; and\n**(B)**\nto develop and offer meaningful threat mitigation advice and actions to enhance\u2014\n**(i)**\nthe defense of, and response to security threats to, the energy sector; and\n**(ii)**\nthe resilience of the United States energy sector;\n**(2)**\nenabling collaboration in the production and exchange of information on threat activity among government and industry to address energy security and resilience and shared energy sector security threats relating to national security, public health, safety, and the economy;\n**(3)**\nimproving detailed understanding of national security risks associated with the energy sector that are or could be exploited by adversaries, including nation-states;\n**(4)**\nachieving a deeper understanding of the tactics, capabilities, and activities of threat actors that have the potential to impact systemic risks to the energy sector; and\n**(5)**\nfacilitating increased collaboration between government and industry, including the sharing of information regarding actual acute threat activity, including incidents, in a secure setting, physical and virtual, to facilitate the energy security and resilience of the United States.\n##### (d) Coordination and integration\nIn carrying out the responsibilities of the Program, the Program shall\u2014\n**(1)**\nalign priorities of and enable support from\u2014\n**(A)**\nthe Department of Homeland Security, including the Cybersecurity and Infrastructure Security Agency;\n**(B)**\nthe Department of Defense, including United States Cyber Command, the National Security Agency, and the Army Interagency Training and Education Center of the National Guard Bureau;\n**(C)**\nthe Department of Justice, including the Federal Bureau of Investigation;\n**(D)**\nthe Office of the Director of National Intelligence; and\n**(E)**\nother Federal agencies and departments, as determined by the Secretary;\n**(2)**\nensure that the processes used by the Program are performed in collaboration with the activities of the Department of Homeland Security and the Department of Defense relating to cybersecurity, including\u2014\n**(A)**\nthe Joint Cyber Defense Collaborative of the Cybersecurity and Infrastructure Security Agency; and\n**(B)**\nthe Cybersecurity Collaboration Center and Enduring Security Framework of the National Security Agency;\n**(3)**\nregularly consult with appropriate representatives of non-Federal entities, such as\u2014\n**(A)**\nState, local, federally recognized Tribal, and territorial governments;\n**(B)**\ninformation sharing and analysis organizations, including information sharing and analysis centers such as the Electricity Information Sharing and Analysis Center; and\n**(C)**\nother appropriate representatives or entities, including private entities, such as manufacturers and vendors, that contribute to the energy sector, as determined by the Secretary;\n**(4)**\nleverage the existing capabilities and services of advanced technology providers, including\u2014\n**(A)**\nNational Laboratories with relevant capabilities;\n**(B)**\ncommercial threat intelligence production and cyber incident response entities; and\n**(C)**\nenergy infrastructure vendors and integrators; and\n**(5)**\nas appropriate, protect information submitted to and shared by the Program consistent with applicable laws, regulations, policies, and procedures.\n##### (e) No right or benefit\n**(1) In general**\nThe provision of assistance or information to governmental or private entities under this section shall be at the sole and unreviewable discretion of the Secretary.\n**(2) Certain assistance or information**\nThe provision of certain assistance or information to a governmental or private entity pursuant to this section shall not create a right or benefit, substantive or procedural, for any other governmental or private entity to similar assistance or information.\n##### (f) Entities of concern\nNo entity of concern (as defined in section 10114(a) of the Research and Development, Competition, and Innovation Act ( 42 U.S.C. 18912(a) )) shall participate in any manner in carrying out the functions of the Program.\n##### (g) Termination\nThe Program shall terminate on the date that is 10 years after the date of enactment of this Act.\n##### (h) Nonapplicability of FACA\nThe Program shall be exempt from complying with the requirements of chapter 10 of title 5, United States Code (including regulations).\n##### (i) Exemption from disclosure\nInformation shared by or with the Federal Government or a State, Tribal, or local government under this Act shall be\u2014\n**(1)**\ndeemed to be voluntarily shared information;\n**(2)**\nexempt from disclosure under section 552 of title 5, United States Code, or any provision of any State, Tribal, or local freedom of information law, open government law, open meetings law, open records law, sunshine law, or similar law requiring the disclosure of information or records; and\n**(3)**\nwithheld from the public, without discretion, under section 552(b)(3) of title 5, United States Code, or any provision of any State, Tribal, or local law requiring the nondisclosure of sensitive information or records.\n##### (j) Report\nThe Secretary shall submit to Congress an annual report that describes, for the year covered by the report\u2014\n**(1)**\nthe achievements of the Program; and\n**(2)**\nareas for improvement with respect to the activities and operations of the Program.\n##### (k) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out this section $50,000,000 for the period of fiscal years 2025 through 2029.",
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
        "name": "Energy",
        "updateDate": "2025-06-13T13:49:52Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1902is.xml"
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
      "title": "ETAP Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-04T03:23:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ETAP Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Energy Threat Analysis Program Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Energy to establish an energy threat analysis program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:50Z"
    }
  ]
}
```
