# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7954?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7954
- Title: Don Young Doug LaMalfa Indian Buffalo Management Act
- Congress: 119
- Bill type: HR
- Bill number: 7954
- Origin chamber: House
- Introduced date: 2026-03-17
- Update date: 2026-05-27T08:05:42Z
- Update date including text: 2026-05-27T08:05:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-17: Introduced in House
- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-05-12 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2026-05-21 - Committee: Subcommittee Hearings Held
- Latest action: 2026-03-17: Introduced in House

## Actions

- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-05-12 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2026-05-21 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-17",
    "latestAction": {
      "actionDate": "2026-03-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7954",
    "number": "7954",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "H001100",
        "district": "3",
        "firstName": "Jeff",
        "fullName": "Rep. Hurd, Jeff [R-CO-3]",
        "lastName": "Hurd",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "Don Young Doug LaMalfa Indian Buffalo Management Act",
    "type": "HR",
    "updateDate": "2026-05-27T08:05:42Z",
    "updateDateIncludingText": "2026-05-27T08:05:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-12",
      "committees": {
        "item": {
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Indian and Insular Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-17",
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
          "date": "2026-03-17T14:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-05-21T18:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-05-12T21:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "systemCode": "hsii00",
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
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "NM"
    },
    {
      "bioguideId": "F000482",
      "district": "0",
      "firstName": "Julie",
      "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Fedorchak",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "ND"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "WA"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "TN"
    },
    {
      "bioguideId": "C001053",
      "district": "4",
      "firstName": "Tom",
      "fullName": "Rep. Cole, Tom [R-OK-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Cole",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "OK"
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
      "sponsorshipDate": "2026-04-16",
      "state": "AK"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "KS"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2026-05-15",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7954ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7954\nIN THE HOUSE OF REPRESENTATIVES\nMarch 17, 2026 Mr. Hurd of Colorado (for himself, Ms. Leger Fernandez , Mrs. Fedorchak , and Mr. Newhouse ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo assist Tribal governments in the management of buffalo and buffalo habitat and the reestablishment of buffalo on Indian land.\n#### 1. Short title\nThis Act may be cited as the Don Young Doug LaMalfa Indian Buffalo Management Act .\n#### 2. Findings; purposes\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nbuffalo sustained a majority of Indian Tribes in North America for many centuries before buffalo were nearly exterminated by non-Indian hunters in the mid-1800s;\n**(2)**\nthe historical, cultural, and spiritual connection between buffalo and Indian Tribes has not diminished over time;\n**(3)**\nIndian Tribes have long desired the reestablishment of buffalo throughout Indian country for cultural, spiritual, and subsistence purposes; and\n**(4)**\nthe successful restoration of buffalo would allow an Indian Tribe to benefit from\u2014\n**(A)**\nthe reintroduction of buffalo into the diets of the members of the Indian Tribe;\n**(B)**\nthe rekindling of the spiritual and cultural relationship between buffalo and the Indian Tribe; and\n**(C)**\nthe use of buffalo for economic development, in the case of an Indian Tribe that chooses to use buffalo for economic development.\n##### (b) Purposes\nThe purposes of this Act are to\u2014\n**(1)**\nfulfill the government-to-government relationship between Tribal Governments and the United States in the management of buffalo and buffalo habitat;\n**(2)**\npromote and develop the capacity of Indian Tribes and Tribal organizations to manage buffalo and buffalo habitat;\n**(3)**\nprotect, conserve, and enhance buffalo, which are important to the subsistence, culture, and economic development of many Indian Tribes;\n**(4)**\npromote the development and use of buffalo and buffalo habitat for the maximum practicable benefit of Indian Tribes and Tribal organizations, through management of buffalo and buffalo habitats in accordance with integrated resource management plans developed by Indian Tribes and Tribal organizations;\n**(5)**\ndevelop buffalo herds and increase production of buffalo in order to meet Tribal subsistence, health, cultural, and economic development needs; and\n**(6)**\npromote the inclusion of Indian Tribes and Tribal organizations in Department of the Interior, local, regional, national, or international\u2014\n**(A)**\ndecision-making processes; and\n**(B)**\nforums.\n#### 3. Definitions\nIn this Act:\n**(1) Buffalo**\nThe term buffalo means an animal of the subspecies Bison bison bison.\n**(2) Buffalo habitat**\nThe term buffalo habitat means Indian land that is managed for buffalo.\n**(3) Department**\nThe term Department means the Department of the Interior.\n**(4) Indian land**\nThe term Indian land has the meaning given the term in paragraph (2) of section 2601 of the Energy Policy Act of 1992 ( 25 U.S.C. 3501 ), except that, in that paragraph, the term Indian reservation shall be considered to have the meaning given the term Indian reservation in paragraph (3) of that section, without regard to the date specified in paragraph (3) of that section.\n**(5) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(6) Secretary**\nThe term Secretary means the Secretary of the Interior.\n**(7) Tribal organization**\nThe term Tribal organization means any legally established organization of Indians that\u2014\n**(A)**\n**(i)**\nis chartered under section 17 of the Act of June 18, 1934 (commonly known as the Indian Reorganization Act ; 25 U.S.C. 5124 ), and recognized by the governing body of one or more Indian Tribes; or\n**(ii)**\nis a Tribal corporation federally chartered under section 3 of the Oklahoma Indian Welfare Act ( 25 U.S.C. 5203 ); and\n**(B)**\nhas demonstrable experience in the restoration of buffalo and buffalo habitat on Indian land.\n#### 4. Buffalo resource management\n##### (a) Direction for coordination\nThe Secretary is directed to work with Indian Tribes and Tribal organizations to\u2014\n**(1)**\npromote and develop the capacity of Indian Tribes and Tribal organizations to manage buffalo and buffalo habitat;\n**(2)**\npromote the ability of Indian Tribes and Tribal organizations to protect, conserve, and enhance populations of buffalo that are owned by Indian Tribes or Tribal organizations;\n**(3)**\npromote the development and use of buffalo and buffalo habitat for the maximum practicable benefit of Indian Tribes and Tribal organizations; and\n**(4)**\npromote the inclusion of Indian Tribes and Tribal organizations in Department, international, national, regional, and local decision making and forums regarding buffalo and buffalo habitat.\n##### (b) Contracts and grants authorized\n**(1) In general**\nThe Secretary shall enter into contracts and cooperative agreements with, and award grants to, Indian Tribes and Tribal organizations to enable the Indian Tribes and Tribal organizations to\u2014\n**(A)**\nplan, conduct, or implement a buffalo restoration or management program;\n**(B)**\nplan and execute commercial activities related to buffalo or buffalo products;\n**(C)**\nsupport the use and deployment of mobile Tribal or Tribal organization meat processing facilities; or\n**(D)**\ncarry out other activities relating to buffalo restoration and management.\n**(2) No diminishment of laws and regulations**\nNothing in this subsection diminishes any Federal or State law (including regulations) regarding diseased buffalo or buffalo that escape from Indian land.\n##### (c) Technical assistance\nThe Secretary shall provide technical assistance to an Indian Tribe or Tribal organization that enters into a contract or cooperative agreement or receives a grant under this section to assist the Indian Tribe or Tribal organization in\u2014\n**(1)**\ncarrying out the activities of a buffalo or buffalo habitat restoration or management program; and\n**(2)**\nimplementing the activities described in subparagraphs (A) through (D) of subsection (b)(1).\n#### 5. Consultation; coordination\n##### (a) Consultation\nNot later than 1 year after the date of enactment of this Act, and on an ongoing basis thereafter, the Secretary shall consult with Indian Tribes and Tribal organizations on initiatives of the Department that affect buffalo or buffalo habitat, including efforts of the Department to contain or eradicate diseased buffalo.\n##### (b) Coordination\nThe Secretary shall develop a policy relating to buffalo and buffalo habitat management activities on Indian land, in accordance with\u2014\n**(1)**\nthe goals and objectives described in buffalo management programs approved by Indian Tribes; and\n**(2)**\nTribal laws and ordinances.\n#### 6. Protection of information\nNotwithstanding any other provision of law, the Secretary shall not disclose or cause to be disclosed any information provided to the Secretary by an Indian Tribe or Tribal organization that is identified by the Indian Tribe or Tribal organization as culturally sensitive, proprietary, or otherwise confidential.\n#### 7. Buffalo from Federal land\n##### (a) In general\nThe Secretary may enter into an agreement with an Indian Tribe or Tribal organization to dispose of surplus buffalo on Federal land administered by the Department, as applicable, by transporting such buffalo onto Indian land.\n##### (b) Application\nAn Indian Tribe or Tribal organization may submit to the Secretary an application to receive buffalo described in subsection (a) at such time, in such manner, and containing such information as the Secretary may require.\n##### (c) Waiver of charges\nThe Secretary may waive any charges for the buffalo described in subsection (a), including any deposit or payment for services as described in section 10.2 of title 36, Code of Federal Regulations (or any successor regulation).\n#### 8. Treaty rights retained\nNothing in this Act alters, modifies, diminishes, or extinguishes the treaty rights of any Indian Tribe.\n#### 9. Sunset\nThe authority provided by this Act ceases to be effective 7 years after the date of the enactment of this Act.",
      "versionDate": "2026-03-17",
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
        "actionDate": "2025-12-15",
        "text": "Read twice and referred to the Committee on Indian Affairs."
      },
      "number": "3478",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Indian Buffalo Management Act",
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
        "name": "Native Americans",
        "updateDate": "2026-04-03T14:57:11Z"
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
      "date": "2026-03-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7954ih.xml"
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
      "title": "Don Young Doug LaMalfa Indian Buffalo Management Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-02T05:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Don Young Doug LaMalfa Indian Buffalo Management Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T05:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To assist Tribal governments in the management of buffalo and buffalo habitat and the reestablishment of buffalo on Indian land.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-02T05:33:33Z"
    }
  ]
}
```
