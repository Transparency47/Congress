# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2998?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2998
- Title: Secure E-Waste Export and Recycling Act
- Congress: 119
- Bill type: HR
- Bill number: 2998
- Origin chamber: House
- Introduced date: 2025-04-24
- Update date: 2026-04-14T10:27:35Z
- Update date including text: 2026-04-14T10:27:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-24: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-04-24: Introduced in House

## Actions

- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-24",
    "latestAction": {
      "actionDate": "2025-04-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2998",
    "number": "2998",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "E000297",
        "district": "13",
        "firstName": "Adriano",
        "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
        "lastName": "Espaillat",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Secure E-Waste Export and Recycling Act",
    "type": "HR",
    "updateDate": "2026-04-14T10:27:35Z",
    "updateDateIncludingText": "2026-04-14T10:27:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-24",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-24",
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
          "date": "2025-04-24T15:08:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "D000600",
      "district": "26",
      "firstName": "Mario",
      "fullName": "Rep. Diaz-Balart, Mario [R-FL-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Diaz-Balart",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "FL"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NY"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "NM"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "PA"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "FL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2998ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2998\nIN THE HOUSE OF REPRESENTATIVES\nApril 24, 2025 Mr. Espaillat (for himself and Mr. Diaz-Balart ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo control the export of electronic waste in order to ensure that such waste does not become the source of counterfeit goods that may reenter military and civilian electronics supply chains in the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Secure E-Waste Export and Recycling Act .\n#### 2. Export controls on electronic waste\n##### (a) Definitions\nIn this section:\n**(1) Electronic waste**\n**(A) In general**\nThe term electronic waste means any of the following used items containing electronic components, or fragments thereof, including parts or subcomponents of such items:\n**(i)**\nComputers and related equipment.\n**(ii)**\nData center equipment (including servers, network equipment, firewalls, battery backup systems, and power distribution units).\n**(iii)**\nMobile computers (including notebooks, netbooks, tablets, and ebook readers).\n**(iv)**\nTelevisions (including portable televisions and portable DVD players).\n**(v)**\nVideo display devices (including monitors, digital picture frames, and portable video devices).\n**(vi)**\nDigital imaging devices (including printers, copiers, facsimile machines, image scanners, and multifunction machines).\n**(vii)**\nConsumer electronics\u2014\n**(I)**\nincluding digital cameras, projectors, digital audio players, cellular phones and wireless internet communication devices, audio equipment, video cassette recorders, DVD players, video game systems (including portable systems), video game controllers, signal converter boxes, and cable and satellite receivers; and\n**(II)**\nnot including appliances that have electronic features.\n**(viii)**\nPortable global positioning system navigation devices.\n**(ix)**\nOther used electronic items that the Secretary determines to be necessary to carry out this section.\n**(B) Exempt items**\nThe term electronic waste does not include\u2014\n**(i)**\nexempted electronic waste items;\n**(ii)**\nelectronic parts of a motor vehicle; or\n**(iii)**\nelectronic components, or items containing electronic components, that are exported or reexported to an entity under the ownership or control of the person exporting or reexporting the components or items, with the intent that the components or items be used for the purpose for which the components or items were used in the United States.\n**(2) Exempted electronic waste items**\n**(A) In general**\nThe term exempted electronic waste items means the following:\n**(i)**\nTested, working used electronics.\n**(ii)**\nLow-risk counterfeit electronics.\n**(iii)**\nRecalled electronics.\n**(B) Definitions**\nIn this paragraph:\n**(i) Tested, working used electronics**\nThe term tested, working used electronics means any used electronic items that\u2014\n**(I)**\nare determined, through testing methodologies established by the Secretary, to be\u2014\n**(aa)**\nfully functional for the purpose for which the items were designed; or\n**(bb)**\nin the case of multifunction devices, fully functional for at least one of the primary purposes for which the items were designed;\n**(II)**\nare exported with the intent to reuse the products as functional products; and\n**(III)**\nare appropriately packaged for shipment to prevent the items from losing functionality as a result of damage during shipment.\n**(ii) Low-risk counterfeit electronics**\nThe term low-risk counterfeit electronics means any electronic components or items that\u2014\n**(I)**\nhave been subjected to destruction processes that render the items unusable for their original purpose; and\n**(II)**\nare exported as a feedstock, with no additional mechanical or hand separation required, in a reclamation process to render the electronic components or items recycled consistent with the laws of the foreign country performing the reclamation process.\n**(iii) Recalled electronics**\nThe term recalled electronics means any electronic items that\u2014\n**(I)**\nbecause of a defect in the design or manufacture of the items\u2014\n**(aa)**\nare subject to a recall notice issued by the Consumer Product Safety Commission or other pertinent Federal authority and have been received by the manufacturer or its agent and repaired by the manufacturer or its agent to cure the defect; or\n**(bb)**\nhave been recalled by the manufacturer as a condition of the validity of the warranty on the items and have been repaired by the manufacturer or its agent to cure the defect; and\n**(II)**\nare exported by the manufacturer of the items.\n**(iv) Feedstock**\nThe term feedstock means any raw material constituting the principal input for an industrial process.\n**(3) Counterfeit good**\nThe term counterfeit good means any good on which, or in connection with which, a counterfeit mark is used.\n**(4) Counterfeit military good**\nThe term counterfeit military good means a counterfeit good that\u2014\n**(A)**\nis falsely identified or labeled as meeting military specifications; or\n**(B)**\nis intended for use in a military or national security application.\n**(5) Counterfeit mark**\nThe term counterfeit mark has the meaning given that term in section 2320 of title 18, United States Code.\n**(6) Export administration regulations**\nThe term Export Administration Regulations means the regulations set forth in subchapter C of chapter VII of title 15, Code of Federal Regulations, or successor regulations.\n**(7) Export; reexport**\nThe terms export and reexport have the meanings given such terms in section 1742 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4801 ).\n**(8) Secretary**\nThe term Secretary means the Secretary of Commerce.\n**(9) Used**\nThe term used , with respect to an item, means the item has been operated or employed.\n##### (b) Prohibition\nExcept as provided in subsections (c) and (d), no person or entity may export or reexport electronic waste or exempted electronic waste items.\n##### (c) Export prohibition exemptions\nA person or entity may export or reexport exempted electronic waste items, but only if the following requirements are met:\n**(1) Registration**\nThe person or entity is listed on a publicly available registry maintained by the Secretary.\n**(2) Filing of export information**\nFor each export transaction, the person or entity files in the Automated Export System, in accordance with part 758 of the Export Administration Regulations (or any corresponding similar regulation or ruling), electronic export information that contains at least the following information:\n**(A)**\nA description of the type and total quantity of exempted electronic waste items exported.\n**(B)**\nThe name of each country that received the exempted electronic waste items for reuse or recycling.\n**(C)**\n**(i)**\nThe name of the ultimate consignee to which the exempted electronic waste items were received for reclamation, recall, or reuse; and\n**(ii)**\ndocumentation and a declaration that such consignee has the necessary permits, resources, and competence to manage the exempted electronic waste items as reusable products or recyclable feedstock and prevent its release as a counterfeit good or counterfeit military good.\n**(3) Compliance with existing laws**\nThe export or reexport of exempted electronic waste items otherwise comply with applicable international agreements to which the United States is a party and with other trade and export control laws of the United States.\n**(4) Export declarations and requirements**\nThe exempted electronic waste items are accompanied by\u2014\n**(A)**\ndocumentation of the registration of the exporter required under paragraph (1);\n**(B)**\na declaration signed by an officer or designated representative of the exporter asserting that the exempted electronic waste items meet the applicable requirements for exempted electronic waste items under this section;\n**(C)**\na description of the contents and condition of the exempted electronic waste items in the shipment;\n**(D)**\nfor tested, working electronics, a description of the testing methodologies and test results for each item;\n**(E)**\nthe name of the ultimate consignee and declaration of the consignee\u2019s applicable permits, resources, and competence to process or use the items as intended; and\n**(F)**\nwith respect to low-risk counterfeit electronics only and when required by the importing country, the written consent of the competent authority of the receiving country to allow the products in such country.\n##### (d) Exception for personal use\nThe Secretary may provide for an exception to the requirements of this section, subject to such recordkeeping requirements as the Secretary may impose, for the export or reexport of 20 or fewer items that are or contain electronic components intended for personal use.\n##### (e) Effective date\n**(1) In general**\nSubject to paragraph (2), this section shall take effect upon the expiration of the 1-year period beginning on the date of the enactment of this Act.\n**(2) Modification of ear**\nThe Secretary shall, not later than the effective date under paragraph (1), ensure that the Export Administration Regulations are modified to carry out this section.\n##### (f) Penalties for violations\nAny person who violates this section or the regulations issued under subsection (e)(2) shall be subject to the same penalties as those that apply to any person violating any other provision of the Export Administration Regulations.",
      "versionDate": "2025-04-24",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-05-29T14:01:57Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-24",
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
          "measure-id": "id119hr2998",
          "measure-number": "2998",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-24",
          "originChamber": "HOUSE",
          "update-date": "2026-04-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2998v00",
            "update-date": "2026-04-14"
          },
          "action-date": "2025-04-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Secure E-Waste Export and Recycling Act</b></p> <p>This bill prohibits the export or reexport of electronic waste, such as computers, televisions, and consumer electronics, subject to certain exemptions (e.g., items that meet specific criteria designed to ensure they do not become the source of counterfeit products).</p>"
        },
        "title": "Secure E-Waste Export and Recycling Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2998.xml",
    "summary": {
      "actionDate": "2025-04-24",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Secure E-Waste Export and Recycling Act</b></p> <p>This bill prohibits the export or reexport of electronic waste, such as computers, televisions, and consumer electronics, subject to certain exemptions (e.g., items that meet specific criteria designed to ensure they do not become the source of counterfeit products).</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119hr2998"
    },
    "title": "Secure E-Waste Export and Recycling Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-24",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Secure E-Waste Export and Recycling Act</b></p> <p>This bill prohibits the export or reexport of electronic waste, such as computers, televisions, and consumer electronics, subject to certain exemptions (e.g., items that meet specific criteria designed to ensure they do not become the source of counterfeit products).</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119hr2998"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2998ih.xml"
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
      "title": "Secure E-Waste Export and Recycling Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Secure E-Waste Export and Recycling Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-07T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To control the export of electronic waste in order to ensure that such waste does not become the source of counterfeit goods that may reenter military and civilian electronics supply chains in the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-07T04:18:24Z"
    }
  ]
}
```
