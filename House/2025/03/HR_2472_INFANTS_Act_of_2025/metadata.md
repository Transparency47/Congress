# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2472?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2472
- Title: INFANTS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2472
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2026-04-30T08:06:31Z
- Update date including text: 2026-04-30T08:06:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2472",
    "number": "2472",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "S001223",
        "district": "13",
        "firstName": "Emilia",
        "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
        "lastName": "Sykes",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "INFANTS Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-30T08:06:31Z",
    "updateDateIncludingText": "2026-04-30T08:06:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:01:45Z",
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
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NJ"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "IL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "DC"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "RI"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2472ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2472\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Mrs. Sykes (for herself, Mr. Pallone , and Mr. Krishnamoorthi ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to ensure the safety of infant and toddler food, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Improving Newborns\u2019 Food and Nutrition Testing Safety Act of 2025 or the INFANTS Act of 2025 .\n#### 2. Definition of infant and toddler food\nSection 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ) is amended by adding at the end the following:\n(tt) The term infant and toddler food means food which purports to be or is represented as food for children up to 24 months of age, including infant formula. .\n#### 3. Contaminants in food\nChapter IV of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 341 et seq. ) is amended by adding at the end the following:\n425. Sampling and testing for contaminants in food (a) Sampling and testing (1) In general The owner, operator, or agent in charge of a food facility that manufactures or processes food, including infant and toddler food, in final product form intended for sale to consumers shall\u2014 (A) collect representative samples of each such food; and (B) conduct testing of the samples for contaminants, including toxic elements. (2) Requirement for sampling plan (A) In general The owner, operator, or agent in charge of a facility described in paragraph (1) shall\u2014 (i) prepare a written sampling plan for all sampling and testing required under this section; and (ii) ensure that all sampling and testing conducted under this section is conducted in accordance with the sampling plan. (B) Requirements A sampling plan under subparagraph (A) shall identify\u2014 (i) the number of sampling units and sample unit size based upon appropriate criteria for identifying, in a representative fashion, the levels of contaminants in each food; and (ii) one or more appropriate test methods and procedures to be used to analyze the samples. (C) Guidance Not later than 18 months after the date of enactment of this section, the Secretary shall issue guidance to assist food facilities in developing sampling plans. Such guidance may, as determined appropriate by the Secretary, address when samples should be tested for specific species of contaminants. (3) Contaminants to be tested Each sample taken pursuant to a sampling plan under this section shall be tested for levels of lead, cadmium, mercury, arsenic, and any other contaminant, including other toxic elements, that the Secretary may specify by regulation. (4) Frequency of testing The sampling and testing conducted under this section shall be conducted at least once per quarter of each calendar year. (5) Foods to be tested The sampling and testing conducted under this section shall be conducted for\u2014 (A) infant and toddler foods, in final package form; and (B) such other foods as the Secretary may specify, by regulation, as appropriate to protect public health. (b) Recordkeeping (1) In general The owner, operator, or agent in charge of a facility described in subsection (a)(1) shall maintain, for not less than 2 years or the shelf-life of each infant and toddler food manufactured or processed at the facility, whichever is longer, records documenting the sampling and testing conducted under this section with respect to the food. (2) Requirements Records required by paragraph (1) to be maintained shall include a detailed description of the foods sampled and tested, the number of samples and tests performed, the size and number of items in each sample unit, a copy of the facility\u2019s sampling plan, identification of the entity conducting the sampling, identification of the entity conducting the testing, and the analytical methods used to perform the sampling and testing. (3) Applicability This subsection applies to all records of sampling and testing conducted under this section, regardless of the findings. (c) Laboratory accreditation The owner, operator, or agent in charge of a food facility described in subsection (a)(1) shall ensure that testing conducted pursuant to this section is performed in accordance with international standards by a laboratory that is accredited by an accreditation body that conforms to international accreditation standards. Testing conducted under this section is not subject to the requirements regarding laboratory accreditation described in section 422. (d) Records availability (1) In general The owner, operator, or agent in charge of a food facility described in subsection (a)(1) shall make all records required under this section available promptly to the Secretary, upon request, for inspection and copying. Upon request of the Secretary, such an owner, operator, or agent in charge shall provide within a reasonable time an English translation of records maintained in a language other than English. (2) Records availability in lieu of an inspection Any records that the Secretary may inspect under this section shall, upon the request of the Secretary, be provided to the Secretary by the owner, operator, or agent in charge of a food facility described in subsection (a)(1), in advance of or in lieu of an inspection, within a reasonable timeframe, within reasonable limits, and in a reasonable manner, and in either electronic or physical form, at the expense of such owner, operator, or agent. The Secretary\u2019s request shall include a sufficient description of the records requested. (3) Confirmation Upon receipt of records requested under paragraph (2), the Secretary shall provide to the person confirmation of receipt. (4) Authority of the Secretary Nothing in this subsection supplants the authority of the Secretary to conduct inspections otherwise permitted under this Act in order to ensure compliance with this Act. (e) Delayed applicability The requirements for sampling and testing under this section apply beginning on the date that is 180 days after the date on which the Secretary publishes the guidance required by subsection (a)(2)(C). .\n#### 4. Adulteration\nSection 402 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 342 ) is amended by adding at the end the following:\n(j) If it is an article of food and the owner, operator, or agent in charge of a food facility that manufactures or processes such food\u2014 (1) is subject to the requirements of section 425; and (2) fails to comply with the requirements of such section with regard to that article. .\n#### 5. Records for or in lieu of certain inspections\nSection 704(a)(4) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 374(a)(4) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (B), (C), and (D) as subparagraphs (C), (D), and (E), respectively;\n**(2)**\nby inserting after subparagraph (A) the following:\n(B) (i) Any records or other information that the Secretary may inspect under authority of this Act from a person that owns or operates an establishment that is engaged in any of the activities described in clause (ii) shall, upon the request of the Secretary, be provided to the Secretary by such person, in advance of or in lieu of an inspection, within a reasonable timeframe, within reasonable limits, and in a reasonable manner, and in either electronic or physical form, at the expense of such person. The Secretary\u2019s request shall include a sufficient description of the records requested. (ii) The activities described in this clause are the following: (I) The manufacturing, processing, packing, transporting, distributing, receiving, holding, or importing of an article of food. (II) The distribution or use of animal feed bearing or containing a veterinary feed directive drug, or the issuance of a veterinary feed directive. ; and\n**(3)**\nby adding at the end the following:\n(F) Section 703 does not apply to requests for records or other information when those requests are made under this section. .\n#### 6. Mandatory recall authority\nSection 423(a) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 350l(a) ) is amended by inserting or if the Secretary determines through any means that an article of infant and toddler food (other than infant formula) bears or contains a contaminant that renders the product adulterated under section 402(a)(1), after animals, .\n#### 7. Report final product positive test results for relevant pathogens in infant formula\nSection 412 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 350a ) is amended\u2014\n**(1)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin the first sentence, by striking promptly and inserting , within 24 hours of acquiring such knowledge, ; and\n**(ii)**\nin the second sentence, by striking the infant formula and inserting an infant formula ;\n**(B)**\nby redesignating paragraph (2) as paragraph (4);\n**(C)**\nin paragraph (4), as so redesignated, by striking paragraph (1) and inserting paragraphs (1) and (2) ; and\n**(D)**\nby inserting after paragraph (1) the following:\n(2) If the result of any in-process or finished product testing of an infant formula that has been processed by the manufacturer is confirmed as a positive analytical result for any environmental pathogen (as defined in section 117.3 of title 21, Code of Federal Regulations (or any successor regulation)), the manufacturer shall\u2014 (A) within 24 hours of acquiring such confirmation, notify the Secretary of such confirmation regardless of whether such infant formula has left an establishment subject to the control of the manufacturer; (B) consult with the Secretary for proper disposal and properly dispose of the affected product; and (C) provide to the Secretary results and isolates from a positive sample of such infant formula. (3) Not later than 90 days after receipt of a notification under paragraph (1) or (2), the Secretary shall confirm through the collection of documentation that the manufacturer submitting the notification performed, or is performing, appropriate corrective action. The manufacturer shall make such documentation available to the Secretary during an inspection and, upon request of the Secretary, electronically or by other means. .\n#### 8. Environmental monitoring\nSection 412 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 350a ) is amended by adding at the end the following:\n(n) Requirements for environmental monitoring for Cronobacter spp and Salmonella (1) In general A manufacturer of powdered infant formula shall establish and implement an environmental monitoring program to verify the effectiveness of sanitation and hygiene controls where the food has the potential to be exposed to Cronobacter spp. or Salmonella. The environmental monitoring program shall be written and include procedures for determining sampling location, number of samples to be taken, and timing and frequency of sample collection and testing. (2) Sampling location and number of samples A manufacturer of powdered infant formula shall ensure that the sampling locations from which samples will be taken, and the number of sites to be tested during routine environmental monitoring pursuant to an environmental monitoring program under paragraph (1), are adequate to determine whether sanitation and hygiene controls are effective. (3) Timing and frequency A manufacturer of powdered infant formula shall ensure that the timing and frequency for collecting testing samples pursuant to an environmental monitoring program under paragraph (1) are adequate to determine whether sanitation and hygiene controls are effective. (4) Records (A) Availability to the Secretary A manufacturer of powdered infant formula shall make all records required under this subsection available promptly to the Secretary, upon request, for inspection and copying. (B) Maintenance Records of environmental monitoring conducted pursuant to this subsection shall be maintained for not less than 2 years or the shelf-life of the infant formula, whichever is longer. (C) Conditions of inspection Any records that the Secretary may inspect under this subsection shall, upon the request of the Secretary, be provided to the Secretary by the manufacturer of powdered infant formula, in advance of or in lieu of an inspection, within a reasonable timeframe, within reasonable limits, and in a reasonable manner, and in either electronic or physical form, at the expense of such manufacturer. The Secretary\u2019s request shall include a sufficient description of the records requested. (D) Confirmation of receipt Upon receipt of records requested under subparagraph (C), the Secretary shall provide to the person confirmation of receipt. (5) Authority of the Secretary Nothing in this subsection supplants the authority of the Secretary to conduct inspections otherwise permitted under this Act in order to ensure compliance with this Act. (6) Delayed applicability The requirements of this subsection apply beginning on the date that is 180 days after the date of enactment of this subsection. (7) Rule of construction Nothing in this subsection shall be construed to exempt an infant formula manufacturer from the requirements of this Act, including the requirements of this section and section 418. .",
      "versionDate": "2025-03-27",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-04-07T12:22:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-27",
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
          "measure-id": "id119hr2472",
          "measure-number": "2472",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-27",
          "originChamber": "HOUSE",
          "update-date": "2026-02-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2472v00",
            "update-date": "2026-02-17"
          },
          "action-date": "2025-03-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Improving Newborns\u2019 Food and Nutrition Testing Safety Act of 2025 or the INFANTS Act of 2025</strong></p><p>This bill requires infant and toddler food to be tested periodically for contaminants and imposes other safety requirements on food and formula manufacturers.</p><p>Specifically, the bill requires facilities that manufacture or process infant and toddler food in final form to conduct quarterly tests for contaminants, including lead and arsenic. The Food and Drug Administration (FDA) may subject other foods to this requirement as appropriate. If a facility that is subject to these requirements fails to comply, food manufactured or processed there is deemed adulterated and may not be introduced into interstate commerce.</p><p>The bill also specifies that if the FDA determines an infant and toddler food, other than infant formula, contains a contaminant that renders the food adulterated, the FDA must provide the responsible party with an opportunity to initiate a voluntary recall. (Under current law, if a responsible party does not voluntarily recall an adulterated product, the FDA may impose a mandatory recall.)</p><p>Further, if testing of an infant formula reveals the presence of certain pathogens, including <em>Listeria monocytogenes</em> or <em>Salmonella</em>, the manufacturer must (1) notify the FDA within 24 hours, (2) properly dispose of the product, and (3) provide the FDA with test results and isolates from the formula.</p><p>Finally, the bill requires manufacturers of powdered infant formula to monitor the effectiveness of sanitation and hygiene controls where the formula has the potential to be exposed to <em>Cronobacter spp</em>. or <em>Salmonella</em>.</p>"
        },
        "title": "INFANTS Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2472.xml",
    "summary": {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Improving Newborns\u2019 Food and Nutrition Testing Safety Act of 2025 or the INFANTS Act of 2025</strong></p><p>This bill requires infant and toddler food to be tested periodically for contaminants and imposes other safety requirements on food and formula manufacturers.</p><p>Specifically, the bill requires facilities that manufacture or process infant and toddler food in final form to conduct quarterly tests for contaminants, including lead and arsenic. The Food and Drug Administration (FDA) may subject other foods to this requirement as appropriate. If a facility that is subject to these requirements fails to comply, food manufactured or processed there is deemed adulterated and may not be introduced into interstate commerce.</p><p>The bill also specifies that if the FDA determines an infant and toddler food, other than infant formula, contains a contaminant that renders the food adulterated, the FDA must provide the responsible party with an opportunity to initiate a voluntary recall. (Under current law, if a responsible party does not voluntarily recall an adulterated product, the FDA may impose a mandatory recall.)</p><p>Further, if testing of an infant formula reveals the presence of certain pathogens, including <em>Listeria monocytogenes</em> or <em>Salmonella</em>, the manufacturer must (1) notify the FDA within 24 hours, (2) properly dispose of the product, and (3) provide the FDA with test results and isolates from the formula.</p><p>Finally, the bill requires manufacturers of powdered infant formula to monitor the effectiveness of sanitation and hygiene controls where the formula has the potential to be exposed to <em>Cronobacter spp</em>. or <em>Salmonella</em>.</p>",
      "updateDate": "2026-02-17",
      "versionCode": "id119hr2472"
    },
    "title": "INFANTS Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Improving Newborns\u2019 Food and Nutrition Testing Safety Act of 2025 or the INFANTS Act of 2025</strong></p><p>This bill requires infant and toddler food to be tested periodically for contaminants and imposes other safety requirements on food and formula manufacturers.</p><p>Specifically, the bill requires facilities that manufacture or process infant and toddler food in final form to conduct quarterly tests for contaminants, including lead and arsenic. The Food and Drug Administration (FDA) may subject other foods to this requirement as appropriate. If a facility that is subject to these requirements fails to comply, food manufactured or processed there is deemed adulterated and may not be introduced into interstate commerce.</p><p>The bill also specifies that if the FDA determines an infant and toddler food, other than infant formula, contains a contaminant that renders the food adulterated, the FDA must provide the responsible party with an opportunity to initiate a voluntary recall. (Under current law, if a responsible party does not voluntarily recall an adulterated product, the FDA may impose a mandatory recall.)</p><p>Further, if testing of an infant formula reveals the presence of certain pathogens, including <em>Listeria monocytogenes</em> or <em>Salmonella</em>, the manufacturer must (1) notify the FDA within 24 hours, (2) properly dispose of the product, and (3) provide the FDA with test results and isolates from the formula.</p><p>Finally, the bill requires manufacturers of powdered infant formula to monitor the effectiveness of sanitation and hygiene controls where the formula has the potential to be exposed to <em>Cronobacter spp</em>. or <em>Salmonella</em>.</p>",
      "updateDate": "2026-02-17",
      "versionCode": "id119hr2472"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2472ih.xml"
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
      "title": "INFANTS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "INFANTS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Improving Newborns\u2019 Food and Nutrition Testing Safety Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to ensure the safety of infant and toddler food, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:17Z"
    }
  ]
}
```
