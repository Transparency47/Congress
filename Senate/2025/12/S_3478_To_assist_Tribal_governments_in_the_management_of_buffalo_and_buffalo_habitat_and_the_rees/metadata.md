# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3478?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3478
- Title: Indian Buffalo Management Act
- Congress: 119
- Bill type: S
- Bill number: 3478
- Origin chamber: Senate
- Introduced date: 2025-12-15
- Update date: 2026-04-03T14:48:46Z
- Update date including text: 2026-04-03T14:48:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-15: Introduced in Senate
- 2025-12-15 - IntroReferral: Introduced in Senate
- 2025-12-15 - IntroReferral: Read twice and referred to the Committee on Indian Affairs.
- Latest action: 2025-12-15: Introduced in Senate

## Actions

- 2025-12-15 - IntroReferral: Introduced in Senate
- 2025-12-15 - IntroReferral: Read twice and referred to the Committee on Indian Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-15",
    "latestAction": {
      "actionDate": "2025-12-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3478",
    "number": "3478",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "H001046",
        "district": "",
        "firstName": "Martin",
        "fullName": "Sen. Heinrich, Martin [D-NM]",
        "lastName": "Heinrich",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Indian Buffalo Management Act",
    "type": "S",
    "updateDate": "2026-04-03T14:48:46Z",
    "updateDateIncludingText": "2026-04-03T14:48:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-15",
      "committees": {
        "item": {
          "name": "Indian Affairs Committee",
          "systemCode": "slia00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Indian Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-15",
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
            "date": "2025-12-15T22:39:35Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-15T22:39:35Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Indian Affairs Committee",
      "systemCode": "slia00",
      "type": "Other"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "OK"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "MN"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3478is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3478\nIN THE SENATE OF THE UNITED STATES\nDecember 15, 2025 Mr. Heinrich (for himself and Mr. Mullin ) introduced the following bill; which was read twice and referred to the Committee on Indian Affairs\nA BILL\nTo assist Tribal governments in the management of buffalo and buffalo habitat and the reestablishment of buffalo on Indian land.\n#### 1. Short title\nThis Act may be cited as the Indian Buffalo Management Act .\n#### 2. Findings; purposes\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nbuffalo sustained a majority of Indian Tribes in North America for many centuries before buffalo were nearly exterminated by non-Indian hunters in the mid-1800s;\n**(2)**\nthe historical, cultural, and spiritual connection between buffalo and Indian Tribes has not diminished over time;\n**(3)**\nIndian Tribes have long desired the reestablishment of buffalo throughout Indian country for cultural, spiritual, and subsistence purposes; and\n**(4)**\nthe successful restoration of buffalo would allow an Indian Tribe to benefit from\u2014\n**(A)**\nthe reintroduction of buffalo into the diets of the members of the Indian Tribe;\n**(B)**\nthe rekindling of the spiritual and cultural relationship between buffalo and the Indian Tribe; and\n**(C)**\nthe use of buffalo for economic development, in the case of an Indian Tribe that chooses to use buffalo for economic development.\n##### (b) Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto fulfill the government-to-government relationship between Tribal governments and the United States in the management of buffalo and buffalo habitat;\n**(2)**\nto promote and develop the capacity of Indian Tribes and Tribal organizations to manage buffalo and buffalo habitat;\n**(3)**\nto protect, conserve, and enhance buffalo, which are important to the subsistence, culture, and economic development of many Indian Tribes;\n**(4)**\nto promote the development and use of buffalo and buffalo habitat for the maximum practicable benefit of Indian Tribes and Tribal organizations, through management of buffalo and buffalo habitats in accordance with integrated resource management plans developed by Indian Tribes and Tribal organizations;\n**(5)**\nto develop buffalo herds and increase production of buffalo in order to meet Tribal subsistence, health, cultural, and economic development needs; and\n**(6)**\nto promote the inclusion of Indian Tribes and Tribal organizations in Department of the Interior, local, regional, national, or international\u2014\n**(A)**\ndecision-making processes; and\n**(B)**\nforums.\n#### 3. Definitions\nIn this Act:\n**(1) Buffalo**\nThe term buffalo means an animal of the subspecies Bison bison bison.\n**(2) Buffalo habitat**\nThe term buffalo habitat means Indian land that is managed for buffalo.\n**(3) Department**\nThe term Department means the Department of the Interior.\n**(4) Indian land**\nThe term Indian land has the meaning given the term in paragraph (2) of section 2601 of the Energy Policy Act of 1992 ( 25 U.S.C. 3501 ), except that, in that paragraph, the term Indian reservation shall be considered to have the meaning given the term Indian reservation in paragraph (3) of that section, without regard to the date specified in paragraph (3) of that section.\n**(5) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(6) Secretary**\nThe term Secretary means the Secretary of the Interior.\n**(7) Tribal organization**\nThe term Tribal organization means any legally established organization of Indians that\u2014\n**(A)**\n**(i)**\nis chartered under section 17 of the Act of June 18, 1934 (commonly known as the Indian Reorganization Act ) (48 Stat. 988, chapter 576; 25 U.S.C. 5124 ), and recognized by the governing body of 1 or more Indian Tribes; or\n**(ii)**\nis a Tribal corporation federally chartered under section 3 of the Act of June 26, 1936 (commonly known as the Oklahoma Indian Welfare Act ) (49 Stat. 1967, chapter 831; 25 U.S.C. 5203 ); and\n**(B)**\nhas demonstrable experience in the restoration of buffalo and buffalo habitat on Indian land.\n#### 4. Buffalo resource management\n##### (a) Direction for coordination\nThe Secretary is directed to work with Indian Tribes and Tribal organizations\u2014\n**(1)**\nto promote and develop the capacity of Indian Tribes and Tribal organizations to manage buffalo and buffalo habitat;\n**(2)**\nto promote the ability of Indian Tribes and Tribal organizations to protect, conserve, and enhance populations of buffalo that are owned by Indian Tribes or Tribal organizations;\n**(3)**\nto promote the development and use of buffalo and buffalo habitat for the maximum practicable benefit of Indian Tribes and Tribal organizations; and\n**(4)**\nto promote the inclusion of Indian Tribes and Tribal organizations in Department, international, national, regional, and local decision making and forums regarding buffalo and buffalo habitat.\n##### (b) Contracts and grants authorized\n**(1) In general**\nThe Secretary shall enter into contracts and cooperative agreements with, and award grants to, Indian Tribes and Tribal organizations to enable the Indian Tribes and Tribal organizations\u2014\n**(A)**\nto plan, conduct, or implement a buffalo restoration or management program;\n**(B)**\nto plan and execute commercial activities related to buffalo or buffalo products;\n**(C)**\nto support the use and deployment of mobile Tribal or Tribal organization meat processing facilities; or\n**(D)**\nto carry out other activities relating to buffalo restoration and management.\n**(2) No diminishment of laws and regulations**\nNothing in this subsection diminishes any Federal or State law (including regulations) regarding diseased buffalo or buffalo that escape from Indian land.\n##### (c) Technical assistance\nThe Secretary shall provide technical assistance to an Indian Tribe or Tribal organization that enters into a contract or cooperative agreement or receives a grant under this section to assist the Indian Tribe or Tribal organization in\u2014\n**(1)**\ncarrying out the activities of a buffalo or buffalo habitat restoration or management program; and\n**(2)**\nimplementing the activities described in subparagraphs (A) through (D) of subsection (b)(1).\n#### 5. Consultation; coordination\n##### (a) Consultation\nNot later than 1 year after the date of enactment of this Act, and on an ongoing basis thereafter, the Secretary shall consult with Indian Tribes and Tribal organizations on initiatives of the Department that affect buffalo or buffalo habitat, including efforts of the Department to contain or eradicate diseased buffalo.\n##### (b) Coordination\nThe Secretary shall develop a policy relating to buffalo and buffalo habitat management activities on Indian land, in accordance with\u2014\n**(1)**\nthe goals and objectives described in buffalo management programs approved by Indian Tribes; and\n**(2)**\nTribal laws and ordinances.\n#### 6. Protection of information\nNotwithstanding any other provision of law, the Secretary shall not disclose or cause to be disclosed any information provided to the Secretary by an Indian Tribe or Tribal organization that is identified by the Indian Tribe or Tribal organization as culturally sensitive, proprietary, or otherwise confidential.\n#### 7. Buffalo from Federal land\n##### (a) In general\nThe Secretary may enter into an agreement with an Indian Tribe or Tribal organization to dispose of surplus buffalo on Federal land administered by the Department, as applicable, by transporting such buffalo onto Indian land.\n##### (b) Application\nAn Indian Tribe or Tribal organization may submit to the Secretary an application to receive buffalo described in subsection (a) at such time, in such manner, and containing such information as the Secretary may require.\n##### (c) Waiver of charges\nThe Secretary may waive any charges for the buffalo described in subsection (a), including any deposit or payment for services as described in section 10.2 of title 36, Code of Federal Regulations (or any successor regulation).\n#### 8. Treaty rights retained\nNothing in this Act alters, modifies, diminishes, or extinguishes the treaty rights of any Indian Tribe.\n#### 9. Sunset\nThe authority provided by this Act ceases to be effective on the date that is 7 years after the date of enactment of this Act.",
      "versionDate": "2025-12-15",
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
        "actionDate": "2026-03-17",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "7954",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Don Young Doug LaMalfa Indian Buffalo Management Act",
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
        "name": "Native Americans",
        "updateDate": "2026-01-09T16:25:38Z"
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
      "date": "2025-12-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3478is.xml"
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
      "title": "Indian Buffalo Management Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-26T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Indian Buffalo Management Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-09T03:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to assist Tribal governments in the management of buffalo and buffalo habitat and the reestablishment of buffalo on Indian land.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-09T03:18:14Z"
    }
  ]
}
```
