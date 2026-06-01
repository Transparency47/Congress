# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/971?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/971
- Title: Chesapeake Bay Conservation Acceleration Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 971
- Origin chamber: Senate
- Introduced date: 2025-03-11
- Update date: 2025-12-05T22:01:02Z
- Update date including text: 2025-12-05T22:01:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-11: Introduced in Senate
- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-03-11: Introduced in Senate

## Actions

- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/971",
    "number": "971",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Chesapeake Bay Conservation Acceleration Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:01:02Z",
    "updateDateIncludingText": "2025-12-05T22:01:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T22:49:09Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "MD"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "PA"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "VA"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "VA"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s971is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 971\nIN THE SENATE OF THE UNITED STATES\nMarch 11, 2025 Mr. Van Hollen (for himself, Ms. Alsobrooks , Mr. Fetterman , Mr. Kaine , and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo provide for the conservation of the Chesapeake Bay, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Chesapeake Bay Conservation Acceleration Act of 2025 .\n#### 2. Chesapeake Bay States Partnership Initiative\nChapter 5 of subtitle D of title XII of the Food Security Act of 1985 is amended by inserting after section 1240M ( 16 U.S.C. 3839bb ) the following:\n1240N. Chesapeake Bay States Partnership Initiative (a) Definitions In this section: (1) Chesapeake Bay watershed The term Chesapeake Bay watershed means\u2014 (A) the Chesapeake Bay; (B) the portions of the States of Delaware, Maryland, New York, Pennsylvania, Virginia, and West Virginia that contain the tributaries, backwaters, and side channels (including their watersheds) that drain into the Chesapeake Bay; and (C) the District of Columbia. (2) Initiative The term Initiative means the Chesapeake Bay States Partnership Initiative established under subsection (b). (b) Establishment and purpose The Secretary shall establish and carry out an initiative, to be known as the Chesapeake Bay States Partnership Initiative , to assist producers in implementing conservation activities on agricultural land in the Chesapeake Bay watershed for the purposes of\u2014 (1) improving water quality and quantity; (2) restoring, enhancing, and preserving soil, air, and related resources; and (3) increasing the resilience of agricultural production to withstand the impacts of climate change. (c) Conservation activities The Secretary shall provide funds made available to carry out the Initiative through applicable programs under this subtitle, including by providing enrollment opportunities that are targeted to the Chesapeake Bay watershed, to assist producers in the Chesapeake Bay watershed in enhancing land and water resources by\u2014 (1) controlling erosion and reducing sediment and nutrient levels in groundwater and surface water; and (2) planning, designing, implementing, and evaluating habitat conservation, restoration, and enhancement measures in cases in which there is significant ecological value if the applicable land is\u2014 (A) retained in the current use of the land; or (B) restored to the natural condition of the land. (d) Considerations In providing funds under the Initiative, the Secretary shall give special consideration to applications\u2014 (1) submitted by producers in the Chesapeake Bay watershed river basins in which nutrient reduction efforts would be most effective; or (2) to carry out conservation activities that reduce nitrogen and sediment, improve management of livestock and waste, or conserve wetlands in the Chesapeake Bay watershed. (e) Duties of Secretary In carrying out the Initiative, the Secretary shall\u2014 (1) as available, use existing plans, models, and assessments to assist producers in implementing conservation activities; and (2) proceed expeditiously to provide funding to producers to implement conservation activities that are consistent with State strategies for the restoration of the Chesapeake Bay watershed. (f) Consultation and coordination The Secretary shall\u2014 (1) in consultation with appropriate Federal agencies, ensure that conservation activities carried out under the Initiative complement Federal, State, and local programs, including programs that address water quality, in the Chesapeake Bay watershed; and (2) in carrying out this section, coordinate with the Farm Service Agency to identify needs and opportunities for buffer management on land subject to a contract under the conservation reserve program under subchapter B of chapter 1 that may be expiring soon. (g) Task Force on Crediting Chesapeake Bay Conservation Investments (1) In general The Secretary and the Administrator of the Environmental Protection Agency shall jointly establish a Federal task force, to be known as the Task Force on Crediting Chesapeake Bay Conservation Investments (referred to in this subsection as the Task Force ). (2) Action plan The Task Force shall develop an action plan that\u2014 (A) identifies improvements to the processes of analyzing, reporting, and quantifying nutrient reductions from conservation activities in the Chesapeake Bay watershed; (B) is responsive to the needs of States in the Chesapeake Bay watershed (including the District of Columbia) and the agricultural community; (C) maintains the scientific integrity of the decisionmaking process and accounting tools under the Chesapeake Bay Program (as defined in section 117(a) of the Federal Water Pollution Control Act ( 33 U.S.C. 1267(a) )); and (D) ensures producer privacy is protected. (3) Identification of opportunities The Task Force shall leverage findings from successful data-sharing pilot projects to identify opportunities to integrate time-saving technologies for the implementation of conservation activities in the Chesapeake Bay watershed. .\n#### 3. Conservation reserve enhancement program participation\n##### (a) Conservation reserve\n**(1) Reauthorization**\nSection 1231(a) of the Food Security Act of 1985 ( 16 U.S.C. 3831(a) ) is amended by striking the 2023 fiscal year and inserting fiscal year 2028 .\n**(2) Eligible land**\nSection 1231(b) of the Food Security Act of 1985 ( 16 U.S.C. 3831(b) ) is amended\u2014\n**(A)**\nin paragraph (6)(B)(ii), by striking or at the end;\n**(B)**\nin paragraph (7)(C), by striking the period at the end and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(8) cropland, marginal pastureland, grasslands, and other rural land that will\u2014 (A) have a positive impact on water quality in furtherance of the goals of the conservation reserve enhancement program under section 1231A; and (B) be devoted to a riparian buffer. .\n**(3) Conservation reserve enhancement program**\nSection 1231A(b) of the Food Security Act of 1985 ( 16 U.S.C. 3831a(b) ) is amended\u2014\n**(A)**\nin paragraph (3), by adding at the end the following:\n(C) Updates (i) In general The Secretary shall provide to each signatory to an agreement under this subsection an option to update the agreement, without renegotiating other provisions of the agreement, to include new incentives made available under this subchapter beginning on January 1, 2018, such as riparian forest buffer management payments. (ii) Matching funds Requirements for matching funds described in paragraph (2)(B) shall not apply to an update to an agreement under clause (i). ; and\n**(B)**\nby adding at the end the following:\n(4) Amendments (A) In general In the case of an amendment to an agreement under this subsection, including an addendum to such an agreement, the Secretary shall\u2014 (i) streamline the amendment process relating to time-sensitive national priorities, including the Chesapeake Bay total maximum daily load; and (ii) give priority to simple amendments to update existing agreements in accordance with paragraph (3)(C). (B) Simple amendments A simple amendment to an agreement described in subparagraph (A)(ii) shall not constitute a renegotiation of the agreement. .\n**(4) Payments**\nSection 1234 of the Food Security Act of 1985 ( 16 U.S.C. 3834 ) is amended\u2014\n**(A)**\nin subsection (b)(4)\u2014\n**(i)**\nby striking In addition and inserting the following:\n(A) In general In addition ; and\n**(ii)**\nby adding at the end the following:\n(B) Minimum payment for certain contracts In the case of a contract updated under section 1231A(b)(3)(C), the incentive payment under subparagraph (A) shall be in an amount that is not less than 40 percent of the actual costs described in that subparagraph. ; and\n**(B)**\nin subsection (g)(1), by striking $50,000 and inserting $100,000 .\n##### (b) Environmental quality incentives program\n**(1) Conservation incentive contracts**\nSection 1240B(j)(2)(C) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20132(j)(2)(C) ) is amended\u2014\n**(A)**\nin clause (i), by striking and at the end;\n**(B)**\nin clause (ii), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(iii) consider participation in the conservation reserve program and the conservation reserve enhancement program under subchapter B of chapter 1, and practices under those programs (such as riparian buffers), in prioritizing grazing practices under the program established by this subchapter with respect to the efficient implementation of grazing systems to holistically address resource concerns. .\n**(2) Evaluation of applications**\nSection 1240C(b) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20133(b) ) is amended\u2014\n**(A)**\nin paragraph (3), by striking and at the end;\n**(B)**\nin paragraph (4), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(5) that would include grazing practices under the program established by this subchapter, in consideration of participation in the conservation reserve program and the conservation reserve enhancement program under subchapter B of chapter 1, and practices under those programs (such as riparian buffers), with respect to the efficient implementation of grazing systems to holistically address resource concerns. .\n#### 4. Chesapeake Bay watershed turnkey pilot program\nSection 1231C of the Food Security Act of 1985 ( 16 U.S.C. 3831c ) is amended by adding at the end the following:\n(c) Chesapeake Bay watershed turnkey pilot program (1) Definitions In this subsection: (A) Chesapeake Bay watershed The term Chesapeake Bay watershed has the meaning given the term in section 1240N(a). (B) CREP definitions The terms CREP , eligible land , and management have the meanings given those terms in section 1231A(a). (C) Eligible practice The term eligible practice means a forested riparian buffer practice under a CREP and any associated activities, including\u2014 (i) a stream crossing; (ii) fencing and alternate water systems; (iii) herbicide applications; and (iv) any other activity that is appropriate to establish the practice. (D) Pilot program The term pilot program means the pilot program established under paragraph (2). (E) Technical service provider The term technical service provider means a third-party provider with which the Secretary enters into an agreement under paragraph (5)(A). (2) Establishment The Secretary shall establish a pilot program under which the Secretary shall provide, for voluntary owners and operators, establishment and management of eligible practices on eligible land located in the Chesapeake Bay watershed that is enrolled through a CREP. (3) Duties of Secretary With respect to eligible land enrolled through the pilot program, the Secretary\u2014 (A) may provide, for the owner or operator, establishment and management of an eligible practice on the eligible land using a technical service provider pursuant to an agreement under paragraph (5); and (B) shall not require the owner or operator\u2014 (i) to pay any costs of the establishment or management of an eligible practice, including any compensation provided under paragraph (5)(C); or (ii) to submit to the Secretary any additional paperwork with respect to the pilot program. (4) Duties of owners and operators Each owner or operator of eligible land enrolled through the pilot program\u2014 (A) shall provide to the Secretary and any technical service providers, as applicable, access to the eligible land for purposes of the establishment or management of an eligible practice under the pilot program; and (B) may not receive any cost-share payment, practice incentive payment, or management payment under this subchapter with respect to an eligible practice under the pilot program. (5) Agreements with technical service providers (A) In general The Secretary may enter into an agreement under section 1242 with 1 or more third-party providers certified under that section, including a third-party provider certified through a streamlined certification process under subsection (e)(5) of that section, that provide technical assistance under this title in the Chesapeake Bay watershed to conduct the establishment and management of an eligible practice on eligible land under the pilot program. (B) Activities In addition to any activity that a technical service provider may conduct pursuant to section 1242 relating to the establishment of an eligible practice, a technical service provider may carry out such activities as are necessary to conduct the establishment and management of an eligible practice under the pilot program. (C) Compensation Under an agreement entered into under subparagraph (A), the Secretary shall provide to a technical service provider reasonable compensation for services provided under the agreement, including administrative assistance, technical assistance, design assistance, and installation costs. (6) Report to Congress Not later than 1 year after the date of enactment of this subsection, the Secretary shall submit to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Agriculture of the House of Representatives a report describing the status of, and any activities carried out under, the pilot program. .\n#### 5. Workforce development\n##### (a) Grants and fellowships for food and agricultural sciences education\n**(1) In general**\nSection 1417 of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3152 ) is amended\u2014\n**(A)**\nin subsection (b)\u2014\n**(i)**\nin the matter preceding paragraph (1), by inserting , junior or community colleges, and postsecondary vocational institutions after other colleges and universities ; and\n**(ii)**\nin paragraph (3), by striking food and agricultural sciences teaching programs, or teaching programs emphasizing and inserting teaching programs, including paid work-based learning, for food and agricultural sciences or ;\n**(B)**\nin subsection (c)\u2014\n**(i)**\nin paragraph (1), by striking and at the end;\n**(ii)**\nin paragraph (2), by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(3) applications for teaching enhancement projects, including paid work-based learning, that address a need for additional trained professionals in food and agricultural sciences or rural economic development, community development, or business development. ;\n**(C)**\nin subsection (j)\u2014\n**(i)**\nby striking paragraph (1); and\n**(ii)**\nby redesignating paragraphs (2) and (3) as paragraphs (1) and (2), respectively;\n**(D)**\nin subsection (l), by striking subsection (j) and inserting subsection (k) ;\n**(E)**\nin subsection (m)\u2014\n**(i)**\nin paragraph (1), by striking and at the end;\n**(ii)**\nin paragraph (2), by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(3) $60,000,000 for each of fiscal years 2026 through 2031. ;\n**(F)**\nby striking subsection (b) each place it appears and inserting subsection (c) ;\n**(G)**\nby redesignating subsections (a) through (m) as subsections (b) through (n), respectively; and\n**(H)**\nby inserting before subsection (b) (as so redesignated) the following:\n(a) Definitions In this section: (1) Institution of higher education The term institution of higher education has the meaning given the term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ). (2) Junior or community college The term junior or community college has the meaning given the term in section 312 of the Higher Education Act of 1965 ( 20 U.S.C. 1058 ). (3) Postsecondary vocational institution The term postsecondary vocational institution has the meaning given the term in section 102(c) of the Higher Education Act of 1965 ( 20 U.S.C. 1002(c) ). (4) Secondary school The term secondary school has the meaning given the term in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ). (5) Work-based learning The term work-based learning has the meaning given the term in section 3 of the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2302 ). .\n**(2) Conforming amendments**\n**(A)**\nSection 708 of the Agriculture, Rural Development, Food and Drug Administration, and Related Agencies Appropriations Act, 1992 ( 7 U.S.C. 2209b ), is amended by striking section 1417(b)(6) of the National Agricultural Research, Extension, and Teaching Policy Act of 1977, as amended ( 7 U.S.C. 3152(b)(6) ) and inserting subsection (c)(6) of section 1417 of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3152 ) .\n**(B)**\nSection 251(f)(1) of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 6971(f)(1) ) is amended\u2014\n**(i)**\nin subparagraph (C)(v), by striking section 1417(b) of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3152(b) ) and inserting subsection (c) of section 1417 of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3152 ) ; and\n**(ii)**\nin subparagraph (D)(v), by striking section 1417(j) of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3152(j) ) and inserting subsection (k) of section 1417 of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3152 ) .\n##### (b) Experienced services program\nSection 1252(a)(2) of the Food Security Act of 1985 ( 16 U.S.C. 3851(a)(2) ) is amended\u2014\n**(1)**\nin subparagraph (D), by striking and at the end;\n**(2)**\nin subparagraph (E), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(F) assisting cooperative initiatives under subsection (c)(3) of section 1417 of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3152 ) to improve higher education teaching programs, including paid work-based learning, at\u2014 (i) land-grant colleges and universities (including the University of the District of Columbia); (ii) colleges and universities having significant minority enrollments and a demonstrable capacity to carry out the teaching of food and agricultural sciences; and (iii) other colleges and universities, junior or community colleges (as defined in section 312 of the Higher Education Act of 1965 ( 20 U.S.C. 1058 )), and postsecondary vocational institutions (as defined in section 102(c) of the Higher Education Act of 1965 ( 20 U.S.C. 1002(c) )) having a demonstrable capacity to carry out the teaching of food and agricultural sciences. .\n##### (c) Competitive, special, and facilities research grants\nSubsection (b) of the Competitive, Special, and Facilities Research Grant Act ( 7 U.S.C. 3157(b) ) is amended\u2014\n**(1)**\nin paragraph (6)(A), by striking teaching and inserting teaching, including paid work-based learning (as defined in section 3 of the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2302 )) ; and\n**(2)**\nin paragraph (7)(B), by inserting , junior or community colleges (as defined in section 312 of the Higher Education Act of 1965 ( 20 U.S.C. 1058 )), and postsecondary vocational institutions (as defined in section 102(c) of the Higher Education Act of 1965 ( 20 U.S.C. 1002(c) )) after colleges and universities .\n#### 6. NRCS direct hire authority\nSection 1242 of the Food Security Act of 1985 ( 16 U.S.C. 3842 ) is amended by adding at the end the following:\n(j) NRCS direct hire authority (1) In general The Secretary may appoint, without regard to the provisions of subchapter I of chapter 33 of title 5, United States Code (other than sections 3303 and 3328 of that title), qualified candidates, as described in paragraph (2), directly to positions within the Natural Resources Conservation Service that provide technical assistance under conservation programs administered by the Natural Resources Conservation Service. (2) Qualifications Paragraph (1) applies to any candidate who\u2014 (A) is qualified to provide the technical assistance described in paragraph (1), as determined by the Secretary; and (B) meets qualification standards established by the Office of Personnel Management. .\n#### 7. Primary regulatory oversight for domestic, wild-caught, invasive catfish\n##### (a) Exemption from oversight\n**(1) Food Safety and Inspection Service**\nSection 1(w)(2) of the Federal Meat Inspection Act ( 21 U.S.C. 601(w)(2) ) is amended by inserting , except for domestic, wild-caught blue catfish (Ictalurus furcatus) and flathead catfish (Pylodictis olivaris) invasive to the Chesapeake Bay ecosystem before the semicolon.\n**(2) USDA grading program**\nSection 203(n)(1) of the Agricultural Marketing Act of 1946 ( 7 U.S.C. 1622(n)(1) ) is amended by inserting , except for domestic, wild-caught blue catfish (Ictalurus furcatus) and flathead catfish (Pylodictis olivaris) invasive to the Chesapeake Bay ecosystem before the semicolon.\n##### (b) Interagency coordination\nNot later than 90 days after the date of enactment of this Act, the Secretary of Agriculture (referred to in this section as the Secretary ) shall execute a memorandum of understanding with the Commissioner of Food and Drugs (referred to in this section as the Commissioner ) for the purpose of transferring primary regulatory oversight of the domestic and import inspection of domestic, wild-caught blue catfish (Ictalurus furcatus) and flathead catfish (Pylodictis olivaris) invasive to the Chesapeake Bay ecosystem from the Secretary to the Commissioner, pursuant to the authorities of the Commissioner under the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 et seq. ), the Fair Packaging and Labeling Act ( 15 U.S.C. 1451 et seq. ), and the Public Health Service Act ( 42 U.S.C. 201 et seq. ).\n##### (c) Regulations\nNot later than 180 days after the date of enactment of this Act, the Secretary, in consultation with the Commissioner, shall issue final regulations to carry out this section and the amendments made by this section in a manner that ensures that there is no duplication in inspection activities relating to domestic, wild-caught blue catfish (Ictalurus furcatus) and flathead catfish (Pylodictis olivaris) invasive to the Chesapeake Bay ecosystem.",
      "versionDate": "2025-03-11",
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
        "actionDate": "2025-03-11",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "2091",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Chesapeake Bay Conservation Acceleration Act of 2025",
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
        "name": "Environmental Protection",
        "updateDate": "2025-05-05T21:02:58Z"
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
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s971is.xml"
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
      "title": "Chesapeake Bay Conservation Acceleration Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-28T11:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Chesapeake Bay Conservation Acceleration Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-28T11:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for the conservation of the Chesapeake Bay, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-28T11:18:36Z"
    }
  ]
}
```
