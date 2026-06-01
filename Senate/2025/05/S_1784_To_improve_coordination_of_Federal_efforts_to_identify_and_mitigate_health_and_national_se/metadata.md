# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1784?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1784
- Title: MAPS Act
- Congress: 119
- Bill type: S
- Bill number: 1784
- Origin chamber: Senate
- Introduced date: 2025-05-15
- Update date: 2026-04-06T20:29:39Z
- Update date including text: 2026-04-06T20:29:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in Senate
- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2025-05-15: Introduced in Senate

## Actions

- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1784",
    "number": "1784",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "P000595",
        "district": "",
        "firstName": "Gary",
        "fullName": "Sen. Peters, Gary C. [D-MI]",
        "lastName": "Peters",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "MAPS Act",
    "type": "S",
    "updateDate": "2026-04-06T20:29:39Z",
    "updateDateIncludingText": "2026-04-06T20:29:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-15",
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
        "item": [
          {
            "date": "2026-03-19T14:00:26Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-05-15T17:56:32Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "OK"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "IA"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "AR"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "VA"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-05-15",
      "state": "ME"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "FL"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1784is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1784\nIN THE SENATE OF THE UNITED STATES\nMay 15, 2025 Mr. Peters (for himself, Mr. Lankford , Ms. Ernst , Mr. Cotton , Mr. Kaine , Mr. King , and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo improve coordination of Federal efforts to identify and mitigate health and national security risks through maintaining a list of essential medicines, conducting a risk assessment of essential medicine supply chains, and creating a monitoring system to map essential medicine supply chains using data analytics.\n#### 1. Short title\nThis Act may be cited as the Mapping America's Pharmaceutical Supply Act or the MAPS Act .\n#### 2. Essential Medicines List\n##### (a) In general\nThe Secretary, in coordination with the heads of other relevant Federal departments and agencies and in consultation with, as appropriate, stakeholders who have relevant expertise, shall update and maintain a list of essential medicines (referred to in this Act as the Essential Medicines List ), initially developed in response to Executive Order 13944 (85 Fed. Reg. 49929), to include active pharmaceutical ingredients and drugs\u2014\n**(1)**\nthat are directly related to responding to chemical, biological, radiological, or nuclear threats and incidents covered by the National Response Framework;\n**(2)**\nof greatest priority for providing health care and identified as being at high risk of shortage;\n**(3)**\nthe shortage of which would have an adverse health outcome on patients with chronic conditions; or\n**(4)**\nthat the Secretary of Defense determines to be critical for military preparedness.\n##### (b) Updates to list\nThe Secretary shall update the Essential Medicines List regularly, on a timeframe that the Secretary determines necessary and appropriate, and not less frequently than every 2 years.\n##### (c) Compilation of initial list\nThe Secretary shall complete the first updates to the Essential Medicines List required pursuant to subsection (a) not later than 180 days after the date of enactment of this Act.\n##### (d) Publication of list\nThe Secretary shall publish the Essential Medicines List promptly after each update pursuant to subsection (b) or (c).\n#### 3. Essential medicines risk assessment\n##### (a) In general\nThe Secretary, in coordination with the Secretary of Defense and in consultation with the heads of other relevant departments and agencies, shall conduct a comprehensive risk assessment of the supply chains for active pharmaceutical ingredients and drugs included on the Essential Medicines List described in section 2.\n##### (b) Contents of essential medicines risk assessment\nAt a minimum, the risk assessment under subsection (a) shall identify, to the extent available\u2014\n**(1)**\nkey starting materials and excipients used in manufacturing the active pharmaceutical ingredients and drugs on the Essential Medicines List;\n**(2)**\nthe active pharmaceutical ingredients and drugs on the Essential Medicines List that rely on a high-risk foreign supplier or foreign entity of concern (as defined in section 9901(8) of the William M. (Mac) Thornberry National Authorization Act for Fiscal Year 2021 ( 15 U.S.C. 4651(8) )) for more than 50 percent of production;\n**(3)**\nthe active pharmaceutical ingredients and drugs on the Essential Medicines List that are sourced exclusively or primarily from foreign establishments, including drugs manufactured domestically from active pharmaceutical ingredients sourced exclusively or primarily from foreign establishments;\n**(4)**\ncurrent domestic manufacturing capabilities for active pharmaceutical ingredients and drugs on the Essential Medicines List, including the key starting materials and excipients of such ingredients and drugs, and any cost-effective manufacturing technologies, including advanced manufacturing;\n**(5)**\npublic health and national security risks, including cybersecurity threats and critical infrastructure designations specific to the supply chains of active pharmaceutical ingredients and drugs included on the Essential Medicines List;\n**(6)**\nany deficiencies, lack of authorities, or limitations in policy or process that reduce the ability of the Federal Government to address any identified public health or national security risks related to supply chains for active pharmaceutical ingredients and drugs included on the Essential Medicines List; and\n**(7)**\nhow the Federal Government will mitigate such national security risks, including through the use of authorities under the Defense Production Act of 1950 ( 50 U.S.C. 4501 et seq. ).\n##### (c) Report on assessment\n**(1) Submission of report**\nNot later than 180 days after the date of enactment of this Act, and annually thereafter, the Secretary, in consultation with the heads of relevant Federal departments and agencies consulted under subsection (a), shall submit a report with the findings under subsection (b) to\u2014\n**(A)**\nthe Committee on Armed Services, the Committee on Health, Education, Labor, and Pensions, and the Committee on Homeland Security and Governmental Affairs of the Senate;\n**(B)**\nthe Committee on Armed Services, the Committee on Energy and Commerce, and the Committee on Homeland Security of the House of Representatives; and\n**(C)**\nthe Office of the Director of National Intelligence.\n**(2) Publication of report**\nNot later than 1 year after the date of enactment of this Act, the Secretary, in consultation with the heads of relevant Federal departments and agencies consulted under subsection (a), shall release a public version of the report submitted under paragraph (1).\n#### 4. U.S. pharmaceutical supply chains mapping\n##### (a) Pharmaceutical supply chain mapping\nThe Secretary of Health and Human Services (referred to in this section as the Secretary ), in coordination with the heads of other relevant Federal departments and agencies, shall ensure coordination of efforts of the Department of Health and Human Services, including through public-private partnerships, to\u2014\n**(1)**\nmap, or otherwise visualize, the supply chains, from manufacturing of key starting materials through manufacturing of finished dosage forms and distribution, of drugs (as defined in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 )) included on the Essential Medicines List under section 2; and\n**(2)**\nuse data analytics to identify supply chain vulnerabilities that pose a threat to national security, as determined by the Secretary or the heads of other relevant Federal departments and agencies.\n##### (b) Requirements\nIn carrying out subsection (a), the Secretary shall\u2014\n**(1)**\ndescribe the roles and responsibilities of agencies and offices within the Department of Health and Human Services related to monitoring such supply chains and assessing any related vulnerabilities; and\n**(2)**\nfacilitate the exchange of information between Federal departments, agencies, and offices, as appropriate and necessary to enable such agencies and offices to carry out roles and responsibilities described in paragraph (1) related to drugs described in subsection (a)(1), which may include\u2014\n**(A)**\nthe location of establishments registered under subsection (b), (c), or (i) of section 510 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360 ) involved in the production of active pharmaceutical ingredients and finished dosage forms of drugs described in subsection (a)(1), and the amount of such ingredients and finished dosage forms produced at each such establishment;\n**(B)**\nto the extent available and as appropriate, the location of establishments so registered involved in the production of the key starting materials and excipients needed to produce the active pharmaceutical ingredients and finished dosage forms, and the amount of such materials and excipients produced at each such establishment; and\n**(C)**\nany regulatory actions with respect to such drugs or the establishments manufacturing such drugs, including with respect to inspections and related regulatory activities conducted under section 704 of such Act ( 21 U.S.C. 374 ), the seizure of such a drug pursuant to section 304 of such Act ( 21 U.S.C. 334 ), any recalls of such a drug; inclusion of such a drug on the drug shortage list under section 506E of such Act ( 21 U.S.C. 356e ), or prior drug shortages reports of a discontinuance or interruption in the production of such a drug under 506C of such Act ( 21 U.S.C. 355d ).\n##### (c) Report\nNot later than 18 months after the date of enactment of this Act, and annually thereafter, the Secretary, in consultation with the heads of agencies with which the Secretary coordinates under subsection (a), shall submit a report to the relevant committees of Congress on\u2014\n**(1)**\nthe current status of efforts to map and analyze pharmaceutical supply chains, as described in subsection (a);\n**(2)**\nactivities of the Secretary carried out under this section to coordinate efforts as described in subsection (a), including information sharing between relevant Federal departments, agencies, and offices;\n**(3)**\nthe roles and responsibilities described in subsection (b)(1), including the identification of any gaps, data limitations, or areas of unnecessary duplication between such roles and responsibilities;\n**(4)**\nthe extent to which Federal agencies use data analytics to conduct predictive modeling of anticipated drug shortages or risks associated with supply chain vulnerabilities that pose a threat to national security; and\n**(5)**\nthe extent to which the Secretary has engaged relevant industry in such mapping.\n#### 5. Department of Defense biannual reports\nNot later than 180 days after the date of enactment of this Act, and every 180 days thereafter, the Secretary of Defense shall submit to the congressional committees described in subparagraphs (A) and (B) of section 3(c)(1) a report that lists all drugs purchased by the Department of Defense during the 180-day period preceding the date of the report\u2014\n**(1)**\nthat contain key starting materials, excipients, or active pharmaceutical ingredients sourced from the People\u2019s Republic of China; or\n**(2)**\nfor which the finished drug product was manufactured in the People\u2019s Republic of China.\n#### 6. Definitions\nIn this Act:\n**(1) Advanced manufacturing**\nThe term advanced manufacturing has the meaning given the term advanced and continuous pharmaceutical manufacturing in section 3016(h) of the 21st Century Cures Act ( 21 U.S.C. 399h(h) ).\n**(2) Cybersecurity threat**\nThe term cybersecurity threat has the meaning given such term in section 2200 of the Homeland Security Act of 2002 ( 6 U.S.C. 650 ).\n**(3) Drug**\nThe term drug has the meaning given such term in section 201(g) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321(g) ).\n**(4) Secretary**\nThe term Secretary , except as otherwise specified, means the Secretary of Health and Human Services.\n#### 7. Additional provisions\n##### (a) Clarification\nThe participation of the Secretary in developing and updating the list of essential medicines under section 2 shall be deemed to be full satisfaction of the requirements applicable to such secretary under section 3 of Executive Order 13944 (85 Fed. Reg. 49929).\n##### (b) Confidential commercial information\nThe exchange of information among the Secretary and the heads of other relevant Federal departments and agencies for purposes of carrying out sections 3 and 4 shall not be a violation of section 1905 of title 18, United States Code. This section shall not be construed to affect the status, if any, of such information as trade secret or confidential commercial information for purposes of section 301(j) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 331(j) ), section 552 of title 5, United States Code, or section 1905 of title 18, United States Code.\n##### (c) Cybersecurity measures\nThe Secretary shall ensure that robust cybersecurity measures are in place to prevent inappropriate access to, or unauthorized disclosure of, the information identified, exchanged, or disclosed under sections 3 and 4.",
      "versionDate": "2025-05-15",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-06-26",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "4191",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "MAPS Act",
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
            "name": "Computer security and identity theft",
            "updateDate": "2026-04-06T20:29:39Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-06T20:27:49Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-06T20:27:36Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-04-06T20:27:41Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2026-04-06T20:29:33Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2026-04-06T20:27:16Z"
          },
          {
            "name": "Strategic materials and reserves",
            "updateDate": "2026-04-06T20:27:33Z"
          },
          {
            "name": "Supply chain",
            "updateDate": "2026-04-06T20:27:27Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-06-02T13:01:17Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1784is.xml"
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
      "title": "MAPS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "MAPS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-30T02:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Mapping America's Pharmaceutical Supply Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-30T02:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve coordination of Federal efforts to identify and mitigate health and national security risks through maintaining a list of essential medicines, conducting a risk assessment of essential medicine supply chains, and creating a monitoring system to map essential medicine supply chains using data analytics.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-30T02:03:31Z"
    }
  ]
}
```
