# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6567?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6567
- Title: Federal Food Administration Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6567
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-04-06T19:31:28Z
- Update date including text: 2026-04-06T19:31:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6567",
    "number": "6567",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000216",
        "district": "3",
        "firstName": "Rosa",
        "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
        "lastName": "DeLauro",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Federal Food Administration Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-06T19:31:28Z",
    "updateDateIncludingText": "2026-04-06T19:31:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
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
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
          "date": "2025-12-10T15:04:05Z",
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
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "CA"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "GA"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "NY"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "IL"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "WI"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "WI"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NJ"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "IN"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "CA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6567ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6567\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Ms. DeLauro (for herself, Ms. Jacobs , and Mr. Bishop ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo establish the Federal Food Administration within the Department of Health and Human Services.\n#### 1. Short title\nThis Act may be cited as the Federal Food Administration Act of 2025 .\n#### 2. Establishment of Federal Food Administration\n##### (a) Establishment\nAs soon as practicable, but not later than 1 year after the date of enactment of this Act, the Secretary of Health and Human Services shall establish within the Department of Health and Human Services an agency to be known as the Federal Food Administration .\n##### (b) Mission\nThe Federal Food Administration shall\u2014\n**(1)**\npromote the public health by promptly and efficiently reviewing food and nutrition research and taking appropriate action on the marketing of regulated products in a timely manner;\n**(2)**\nwith respect to such products, protect the public health by ensuring that foods are safe, wholesome, sanitary, and properly labeled;\n**(3)**\nparticipate through appropriate processes with representatives of other countries to protect public health and promote fair trade practices in food; and\n**(4)**\nas determined to be appropriate by the Secretary, carry out paragraphs (1) through (3) in consultation with experts in science, medicine, and public health, and in cooperation with consumers, users, manufacturers, importers, packers, distributors, and retailers of regulated products.\n##### (c) Interagency collaboration\nThe Secretary shall implement programs and policies that will foster collaboration between the Federal Food Administration, the Department of Agriculture, the Centers for Disease Control and Prevention, the National Institutes of Health, and other science-based Federal agencies, to enhance the scientific and technical expertise available to the Secretary in the conduct of the duties of the Secretary with respect to the development, investigation, evaluation, and postmarket monitoring of food.\n##### (d) Commissioner of Foods\n**(1) In general**\nThe Federal Food Administration shall be headed by the Commissioner of Foods, who shall be appointed by the President, by and with the advice and consent of the Senate.\n**(2) General powers**\nThe Secretary, acting through the Commissioner of Foods, shall be responsible for\u2014\n**(A)**\nproviding overall direction to the Federal Food Administration and establishing and implementing general policies respecting the management and operation of programs and activities of the Federal Food Administration;\n**(B)**\ncoordinating and overseeing the operation of all administrative entities within the Federal Food Administration;\n**(C)**\nresearch relating to foods in carrying out the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 et seq. );\n**(D)**\nconducting educational and public information programs relating to the responsibilities of the Federal Food Administration; and\n**(E)**\nperforming such other functions as the Secretary may prescribe.\n##### (e) Technical and scientific review groups\nThe Secretary, acting through the Commissioner of Foods, may, without regard to the provisions of title 5, United States Code, governing appointments in the competitive service and without regard to the provisions of chapter 51 and subchapter III of chapter 53 of such title relating to classification and General Schedule pay rates, establish such technical and scientific review groups as are needed to carry out the functions of the Federal Food Administration, including functions under the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 et seq. ) relating to food, and appoint and pay the members of such groups, except that officers and employees of the United States shall not receive additional compensation for service as members of such groups.\n#### 3. Inspection of food facilities\n##### (a) Establishment of inspection program\n**(1) In general**\nThe Commissioner of Foods shall establish an inspection program, which shall include inspections of food facilities in accordance with subsection (b), subject to the facility category determined in accordance with the guidance issued under paragraph (2).\n**(2) Facility categories**\nAs soon as practicable, but not later than 1 year after the date of enactment of this Act, the Commissioner of Foods shall issue formal guidance defining the criteria by which food facilities will be divided into high-risk , intermediate risk , and low-risk facilities.\n##### (b) Inspections of food facilities\n**(1) Frequency of inspections**\n**(A) High-risk facilities**\nThe Commissioner of Foods shall inspect high-risk facilities not less frequently than annually.\n**(B) Intermediate-risk facilities**\nThe Commissioner of Foods shall inspect intermediate-risk facilities not less frequently than once every 2 years.\n**(C) Low-risk facilities**\nThe Commissioner of Foods shall inspect low-risk facilities, which shall include warehouses or similar facilities that engage in packaging or distribution, and pose very minimal public health risk, not less frequently than once every 3 years.\n**(2) Infant formula manufacturing facilities**\nThe Commissioner of Foods shall inspect the facilities of each manufacturer of infant formula not less frequently than every 6 months.\n##### (c) Federal and State cooperation\nThe Commissioner of Foods shall contract with State officials to carry out not less than half of the inspections required under this section.\n##### (d) Compliance checks\nNot later than 30 days after issuing to a facility a form that is equivalent to FDA Form 483, pursuant to an inspection conducted under section 704 of Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 374 ), the Commissioner of Foods shall conduct a follow-up compliance check of the facility.\n#### 4. Transfer of authority, functions and agencies\n##### (a) Transfer of authority\nThe Federal Food Administration shall assume responsibility for carrying out the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 et seq. ), as related to food, and shall assume and maintain all regulatory, administrative, and enforcement authorities with respect to food held by the Food and Drug Administration on the date of enactment of this Act.\n##### (b) Transfer of functions\nFor each Federal agency, office, and center specified in subsection (c), there are transferred to the Federal Food Administration all functions that the head of the Federal agency exercised on the day before the date of enactment of this Act (including all related functions of any officer or employee of the Federal agency) that relate to the regulation of food or the administration or enforcement of food law, as determined by the President.\n##### (c) Transferred agencies\nThe Federal agencies referred to in subsection (b) are\u2014\n**(1)**\nthe resources and facilities of the Human Foods Program of the Food and Drug Administration for purposes of administering the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 et seq. ) with respect to food;\n**(2)**\nthe resources and facilities of the Office of Inspections and Investigations of the Food and Drug Administration for purposes of administering the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 et seq. ) with respect to food;\n**(3)**\nthe resources and facilities of the Center for Veterinary Medicine of the Food and Drug Administration for purposes of administering the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 et seq. ) with respect to food; and\n**(4)**\nsuch other offices, services, or agencies as the President designates by executive order to carry out this Act.\n##### (d) Conforming amendment\nSubchapter A of chapter VII of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 371 et seq. ) is amended by adding at the end the following:\n716. Regulation of food Notwithstanding any other provision of this Act, beginning as soon as practicable but not later than the date that is 1 year after the date of enactment of the Federal Food Administration Act of 2025 \u2014 (1) any authority under this Act that relates to food shall be under the authority of the Federal Food Administration, and shall be carried out by the Commissioner of Foods described in section 2(d) of the Federal Food Administration Act of 2025 ; and (2) any reference in this Act to authorities related to food held by the Commissioner of Food and Drugs, including any reference in this Act to such authorities held by the Secretary, acting through the Commissioner of Food and Drugs, shall be deemed to be a reference to authorities held by the Commissioner of Foods, or by the Secretary, acting through the Commissioner of Foods, as appropriate. .\n#### 5. Funding\n##### (a) Transfer of funds\nThe appropriations, allocations, and other funds that relate to the authorities, functions and agencies transferred under section 4 shall be transferred to the Federal Food Administration.\n##### (b) Authorization of appropriations\nThere are authorized to be appropriated to carry out this section, such sums as may be necessary for fiscal year 2026 and each fiscal year thereafter.\n#### 6. Definitions\nIn this Act:\n**(1) Commissioner of Foods**\nThe term Commissioner of Foods means the Commissioner described in section 2(d).\n**(2) Facility**\nThe term facility means any factory, warehouse, or establishment that is subject to the requirements of section 415 or 419 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 350d ; 350h).\n**(3) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.",
      "versionDate": "2025-12-10",
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
        "actionDate": "2025-06-24",
        "text": "Received in the Senate and Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "3422",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Promoting Opportunities for Non-Traditional Capital Formation Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-10",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S8626)"
      },
      "number": "3422",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Federal Food Administration Act of 2025",
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
        "name": "Health",
        "updateDate": "2026-01-07T17:49:26Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6567ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the Federal Food Administration within the Department of Health and Human Services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-29T14:18:23Z"
    },
    {
      "title": "Federal Food Administration Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-29T14:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Food Administration Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-29T14:08:21Z"
    }
  ]
}
```
