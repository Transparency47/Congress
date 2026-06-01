# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4191?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4191
- Title: MAPS Act
- Congress: 119
- Bill type: HR
- Bill number: 4191
- Origin chamber: House
- Introduced date: 2025-06-26
- Update date: 2026-04-21T20:28:55Z
- Update date including text: 2026-04-21T20:28:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-26: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-06-26: Introduced in House

## Actions

- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4191",
    "number": "4191",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001163",
        "district": "7",
        "firstName": "Doris",
        "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
        "lastName": "Matsui",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "MAPS Act",
    "type": "HR",
    "updateDate": "2026-04-21T20:28:55Z",
    "updateDateIncludingText": "2026-04-21T20:28:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-26",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T14:07:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4191ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4191\nIN THE HOUSE OF REPRESENTATIVES\nJune 26, 2025 Ms. Matsui (for herself and Mr. Crenshaw ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo improve coordination of Federal efforts to identify and mitigate health and national security risks through maintaining a list of essential medicines, conducting a risk assessment of essential medicine supply chains, and creating a monitoring system to map essential medicine supply chains using data analytics.\n#### 1. Short title\nThis Act may be cited as the Mapping America\u2019s Pharmaceutical Supply Act or the MAPS Act .\n#### 2. Essential medicines list\n##### (a) In general\nThe Secretary, in coordination with the heads of other relevant Federal departments and agencies and in consultation with, as appropriate, stakeholders who have relevant expertise, shall update and maintain a list of essential medicines (referred to in this Act as the Essential Medicines List ), initially developed in response to Executive Order 13944 (85 Fed. Reg. 49929), to include active pharmaceutical ingredients and drugs\u2014\n**(1)**\nthat are directly related to responding to chemical, biological, radiological, or nuclear threats and incidents covered by the National Response Framework;\n**(2)**\nof greatest priority for providing health care and identified as being at high risk of shortage; or\n**(3)**\nthe shortage of which would have an adverse health outcome on patients with chronic conditions.\n##### (b) Updates to list\nThe Secretary shall review the Essential Medicines List regularly, on a timeframe that the Secretary determines necessary and appropriate, and not less frequently than every 2 years; and shall update the Essential Medicines List as necessary based on the findings of such review.\n##### (c) Compilation of initial list\nThe Secretary shall complete the first updates to the Essential Medicines List required pursuant to subsection (a) not later than 180 days after the date of enactment of this Act.\n##### (d) Publication of list\nThe Secretary shall publish the Essential Medicines List promptly after each update pursuant to subsection (b) or (c).\n#### 3. Essential medicines risk assessment\n##### (a) In general\nThe Secretary, in consultation with the heads of other relevant departments and agencies, shall conduct a comprehensive risk assessment of the supply chains for active pharmaceutical ingredients and drugs included on the Essential Medicines List described in section 2.\n##### (b) Contents of essential medicines risk assessment\nAt a minimum, the risk assessment under subsection (a) shall identify, to the extent available\u2014\n**(1)**\nkey starting materials and excipients used in manufacturing the active pharmaceutical ingredients and drugs on the Essential Medicines List;\n**(2)**\nthe active pharmaceutical ingredients and drugs on the Essential Medicines List that rely on a foreign supplier for more than 50 percent of production;\n**(3)**\nthe active pharmaceutical ingredients and drugs on the Essential Medicines List that are sourced exclusively or primarily from a single supplier, including drugs manufactured domestically from active pharmaceutical ingredients sourced exclusively or primarily from a single supplier;\n**(4)**\ncurrent domestic manufacturing capabilities for active pharmaceutical ingredients and drugs on the Essential Medicines List, including the key starting materials and excipients of such ingredients and drugs, and any cost-effective manufacturing technologies, including advanced manufacturing;\n**(5)**\npublic health and national security risks, including cybersecurity threats and critical infrastructure designations specific to the supply chains of active pharmaceutical ingredients and drugs included on the Essential Medicines List;\n**(6)**\nany deficiencies, lack of authorities, or limitations in policy or process that reduce the ability of the Federal Government to address any identified public health or national security risks related to supply chains for active pharmaceutical ingredients and drugs included on the Essential Medicines List; and\n**(7)**\nhow the Federal Government will mitigate such national security risks, including through the use of authorities under the Defense Production Act of 1950 ( 50 U.S.C. 4501 et seq. ).\n##### (c) Report on assessment\n**(1) Submission of report**\nNot later than 180 days after the date of enactment of this Act, and annually thereafter, the Secretary, in consultation with the heads of relevant Federal departments and agencies consulted under subsection (a), shall submit a report with the findings under subsection (b) to the relevant Committees of Congress.\n#### 4. U. S . pharmaceutical supply chains mapping\n##### (a) Pharmaceutical supply chain mapping\nThe Secretary of Health and Human Services (referred to in this section as the Secretary ), in coordination with the heads of other relevant Federal departments and agencies, shall ensure coordination of efforts of the Department of Health and Human Services, including through public-private partnerships, to\u2014\n**(1)**\nmap, or otherwise visualize, the supply chains, from manufacturing of key starting materials through manufacturing of finished dosage forms and distribution, of drugs (as defined in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 )) included on the Essential Medicines List under section 2; and\n**(2)**\nuse data analytics to identify supply chain vulnerabilities that pose a threat to public health or national security, as determined by the Secretary or the heads of other relevant Federal departments and agencies.\n##### (b) Requirements\nIn carrying out subsection (a), the Secretary shall\u2014\n**(1)**\ndescribe the roles and responsibilities of agencies and offices within the Department of Health and Human Services related to monitoring such supply chains and assessing any related vulnerabilities; and\n**(2)**\nfacilitate the exchange of information between Federal departments, agencies, and offices, as appropriate and necessary to enable such agencies and offices to carry out roles and responsibilities described in paragraph (1) related to drugs described in subsection (a)(1). Such information should include, at a minimum\u2014\n**(A)**\nthe location of establishments registered under subsection (b), (c), or (i) of section 510 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360 ) involved in the production of active pharmaceutical ingredients and finished dosage forms of drugs described in subsection (a)(1), and the amount of such ingredients and finished dosage forms produced at each such establishment;\n**(B)**\nto the extent available and as appropriate, the location of establishments so registered involved in the production of the key starting materials and excipients needed to produce the active pharmaceutical ingredients and finished dosage forms, and the amount of such materials and excipients produced at each such establishment; and\n**(C)**\nany regulatory actions with respect to such drugs or the establishments manufacturing such drugs, including with respect to inspections and related regulatory activities conducted under section 704 of such Act ( 21 U.S.C. 374 ), the seizure of such a drug pursuant to section 304 of such Act ( 21 U.S.C. 334 ), any recalls of such a drug; inclusion of such a drug on the drug shortage list under section 506E of such Act ( 21 U.S.C. 356e ), or prior reports of a discontinuance or interruption in the production of such a drug under section 506C of such Act ( 21 U.S.C. 356c ).\n##### (c) Report\nNot later than 18 months after the date of enactment of this Act, and annually thereafter, the Secretary, in consultation with the heads of agencies with which the Secretary coordinates under subsection (a), shall submit a report to the relevant committees of Congress on\u2014\n**(1)**\nthe current status of efforts to map and analyze pharmaceutical supply chains, as described in subsection (a);\n**(2)**\nactivities of the Secretary carried out under this section to coordinate efforts as described in subsection (a), including information sharing between relevant Federal departments, agencies, and offices;\n**(3)**\nthe roles and responsibilities described in subsection (b)(1), including the identification of any gaps, data limitations, or areas of unnecessary duplication between such roles and responsibilities;\n**(4)**\nthe extent to which Federal agencies use data analytics to conduct predictive modeling of anticipated drug shortages or risks associated with supply chain vulnerabilities that pose a threat to national security; and\n**(5)**\nthe extent to which the Secretary has engaged relevant industry in such mapping.\n#### 5. Definitions\nIn this Act:\n**(1) Advanced manufacturing**\nThe term advanced manufacturing has the meaning given the term advanced and continuous pharmaceutical manufacturing in section 3016(h) of the 21st Century Cures Act ( 21 U.S.C. 399h(h) ).\n**(2) Cybersecurity threat**\nThe term cybersecurity threat has the meaning given such term in section 2200 of the Homeland Security Act of 2002 ( 6 U.S.C. 650 ).\n**(3) Drug**\nThe term drug has the meaning given such term in section 201(g) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321(g) ).\n**(4) Secretary**\nThe term Secretary , except as otherwise specified, means the Secretary of Health and Human Services.\n#### 6. Additional provisions\n##### (a) Clarification\nThe participation of the Secretary in developing and updating the list of essential medicines under section 2 shall be deemed to be full satisfaction of the requirements applicable to such Secretary under section 3 of Executive Order 13944 (85 Fed. Reg. 49929).\n##### (b) Confidential commercial information\nThe exchange of information among the Secretary and the heads of other relevant Federal departments and agencies for purposes of carrying out sections 3 and 4 shall not be a violation of section 1905 of title 18, United States Code. This section shall not be construed to affect the status, if any, of such information as trade secret or confidential commercial information for purposes of section 301(j) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 331(j) ), section 552 of title 5, United States Code, or section 1905 of title 18, United States Code.\n##### (c) Cybersecurity measures\nThe Secretary shall ensure that robust cybersecurity measures are in place to prevent inappropriate access to, or unauthorized disclosure of, the information identified, exchanged, or disclosed under sections 3 and 4.",
      "versionDate": "2025-06-26",
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
        "actionDate": "2026-03-19",
        "text": "Committee on Health, Education, Labor, and Pensions. Hearings held."
      },
      "number": "1784",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "MAPS Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Computer security and identity theft",
            "updateDate": "2026-04-06T20:30:01Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-06T20:30:01Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-06T20:30:01Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-04-06T20:30:01Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2026-04-06T20:30:01Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2026-04-06T20:30:01Z"
          },
          {
            "name": "Strategic materials and reserves",
            "updateDate": "2026-04-06T20:30:01Z"
          },
          {
            "name": "Supply chain",
            "updateDate": "2026-04-06T20:30:01Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-09-18T19:53:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-26",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr4191",
          "measure-number": "4191",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-26",
          "originChamber": "HOUSE",
          "update-date": "2026-04-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4191v00",
            "update-date": "2026-04-21"
          },
          "action-date": "2025-06-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Mapping America\u2019s Pharmaceutical Supply Act or the MAPS Act</strong></p><p>This bill requires the Food and Drug Administration (FDA) to continually update its essential medicines list and identify risks and vulnerabilities in the associated supply chains.</p><p>In 2020, in response to an executive order, the FDA published a list of essential medicines deemed medically necessary to have available at all times. The bill requires the FDA to update and maintain this list to include drugs and ingredients (1) related to responding to public health threats and emergency incidents, (2) that are of greatest priority for providing health care and are at high risk of shortage, and (3) the shortage of which would adversely affect patients with chronic conditions. The FDA must review the list\u00a0at least every two years and update it as appropriate.</p><p>Also, the bill requires the FDA to conduct a risk assessment of the supply chains for drugs and ingredients on the list and annually report its findings to Congress. The assessment must include information about key manufacturing materials, drugs with primarily foreign or single suppliers, manufacturing capacity, relevant public health and national security risks, and risk mitigation strategies.</p><p>Additionally, the Department of Health and Human Services (HHS) must map and monitor relevant supply chains to identify vulnerabilities and provide an annual status report to Congress. HHS must facilitate the secure exchange of information among agencies regarding locations and quantities of production and relevant regulatory actions.</p>"
        },
        "title": "MAPS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4191.xml",
    "summary": {
      "actionDate": "2025-06-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Mapping America\u2019s Pharmaceutical Supply Act or the MAPS Act</strong></p><p>This bill requires the Food and Drug Administration (FDA) to continually update its essential medicines list and identify risks and vulnerabilities in the associated supply chains.</p><p>In 2020, in response to an executive order, the FDA published a list of essential medicines deemed medically necessary to have available at all times. The bill requires the FDA to update and maintain this list to include drugs and ingredients (1) related to responding to public health threats and emergency incidents, (2) that are of greatest priority for providing health care and are at high risk of shortage, and (3) the shortage of which would adversely affect patients with chronic conditions. The FDA must review the list\u00a0at least every two years and update it as appropriate.</p><p>Also, the bill requires the FDA to conduct a risk assessment of the supply chains for drugs and ingredients on the list and annually report its findings to Congress. The assessment must include information about key manufacturing materials, drugs with primarily foreign or single suppliers, manufacturing capacity, relevant public health and national security risks, and risk mitigation strategies.</p><p>Additionally, the Department of Health and Human Services (HHS) must map and monitor relevant supply chains to identify vulnerabilities and provide an annual status report to Congress. HHS must facilitate the secure exchange of information among agencies regarding locations and quantities of production and relevant regulatory actions.</p>",
      "updateDate": "2026-04-21",
      "versionCode": "id119hr4191"
    },
    "title": "MAPS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Mapping America\u2019s Pharmaceutical Supply Act or the MAPS Act</strong></p><p>This bill requires the Food and Drug Administration (FDA) to continually update its essential medicines list and identify risks and vulnerabilities in the associated supply chains.</p><p>In 2020, in response to an executive order, the FDA published a list of essential medicines deemed medically necessary to have available at all times. The bill requires the FDA to update and maintain this list to include drugs and ingredients (1) related to responding to public health threats and emergency incidents, (2) that are of greatest priority for providing health care and are at high risk of shortage, and (3) the shortage of which would adversely affect patients with chronic conditions. The FDA must review the list\u00a0at least every two years and update it as appropriate.</p><p>Also, the bill requires the FDA to conduct a risk assessment of the supply chains for drugs and ingredients on the list and annually report its findings to Congress. The assessment must include information about key manufacturing materials, drugs with primarily foreign or single suppliers, manufacturing capacity, relevant public health and national security risks, and risk mitigation strategies.</p><p>Additionally, the Department of Health and Human Services (HHS) must map and monitor relevant supply chains to identify vulnerabilities and provide an annual status report to Congress. HHS must facilitate the secure exchange of information among agencies regarding locations and quantities of production and relevant regulatory actions.</p>",
      "updateDate": "2026-04-21",
      "versionCode": "id119hr4191"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4191ih.xml"
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
      "title": "MAPS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-12T04:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MAPS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Mapping America\u2019s Pharmaceutical Supply Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve coordination of Federal efforts to identify and mitigate health and national security risks through maintaining a list of essential medicines, conducting a risk assessment of essential medicine supply chains, and creating a monitoring system to map essential medicine supply chains using data analytics.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-12T04:18:43Z"
    }
  ]
}
```
