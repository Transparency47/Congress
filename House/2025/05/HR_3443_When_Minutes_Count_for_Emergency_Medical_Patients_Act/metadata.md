# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3443?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3443
- Title: When Minutes Count for Emergency Medical Patients Act
- Congress: 119
- Bill type: HR
- Bill number: 3443
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2026-04-21T08:05:40Z
- Update date including text: 2026-04-21T08:05:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-15 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-15 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3443",
    "number": "3443",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001067",
        "district": "9",
        "firstName": "Richard",
        "fullName": "Rep. Hudson, Richard [R-NC-9]",
        "lastName": "Hudson",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "When Minutes Count for Emergency Medical Patients Act",
    "type": "HR",
    "updateDate": "2026-04-21T08:05:40Z",
    "updateDateIncludingText": "2026-04-21T08:05:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T14:07:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-15T14:07:35Z",
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
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "MI"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "NJ"
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
      "sponsorshipDate": "2026-03-03",
      "state": "DC"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "PA"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "PA"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3443ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3443\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Hudson (for himself and Mrs. Dingell ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XI of the Social Security Act to create a model, and to direct the Medicare Payment Advisory Commission to carry out a study and report with respect to Medicare payment for emergency medical services.\n#### 1. Short title\nThis Act may be cited as the When Minutes Count for Emergency Medical Patients Act .\n#### 2. CMI emergency services payment model\nSection 1115A of the Social Security Act ( 42 U.S.C. 1315a ) is amended\u2014\n**(1)**\nin subsection (b)(2)\u2014\n**(A)**\nin subparagraph (A), in the third sentence, by inserting , and shall include the model described in subparagraph (B)(xxviii) before the period at the end; and\n**(B)**\nin subparagraph (B), by adding at the end the following new clause:\n(xxviii) The When Minutes Count for EMS Patients Model described in subsection (h). ; and\n**(2)**\nby adding at the end the following new subsection:\n(h) When Minutes Count for EMS Patients Model (1) In general For purposes of subsection (b)(2)(B)(xxviii), the When Minutes Count for EMS Patients Model described in this subsection is a model that provides supplemental payment for ground and air ambulance services under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ) for specified life-sustaining EMS medications and blood products that require immediate administration by EMS professionals to individuals with emergency medical conditions (as defined in section 1867(e)). (2) Application and selection of eligible entities (A) Application (i) In general To be eligible to participate in the model described in paragraph (1) , an eligible entity shall submit to the Secretary an application in such form, at such time, and containing such information as the Secretary may determine appropriate, which shall include at least the information described in clause (ii). (ii) Information described For purposes of clause (i), the information described in this clause is such information as the Secretary determines necessary to demonstrate that the eligible entity will be able to provide sufficient data for the Secretary to be able to perform the analysis required for the report required under paragraph (5), including\u2014 (I) data that encompasses quality of care and the outcomes of individuals receiving emergency medical services (as defined in 303(k)(13)(C) of the Controlled Substances Act); and (II) discrete data elements associated with emergency department and inpatient services, including ICD\u201310 and National Emergency Medical Services Information System (NEMSIS) dispositions (NEMSIS 3.5 elements: eOutcome 0.1, eOutcome 0.2, eOutcome 10, and eOutcome 13). (B) Selection The Secretary, in approving applications under this subparagraph\u2014 (i) shall select not less than 1 eligible entity in each HHS region (as determined by the Secretary); and (ii) to the extent feasible, shall select at least 1 of each type of emergency medical services agency (as such term is defined for purposes of section 303(k)(13)(D) of the Controlled Substances Act). (3) Supplemental payment adjustments The Secretary shall set payment rates for services furnished under the model described in paragraph (1) and shall make such payments in addition to any payments that eligible entities participating in the model receive for such services under section 1834 of this title. Such payment rates shall\u2014 (A) be calculated based on the total costs of\u2014 (i) maintaining a sufficient supply of specified EMS medications to minimize EMS medical directors having to routinely change protocols for administration of such medications due to their persistent shortages (which shall constitute at least double the amount of average actual acquisition for such medications in the first year of the model, as determined necessary by the Secretary to ensure such sufficient supply); (ii) blood products (calculated separately for each type of product used in the provision of emergency medical services, taking into account the cost of the acquisition, storage, maintenance, transport by ground and air, and administration of blood products; and administrative costs associated with blood and blood product usage and storage, including wastage; (iii) maintaining a sufficient supply to serve all patients requiring the administration of specified EMS medications and blood products in the eligible entity\u2019s primary service area (which shall not be based on the actual administration of such medications and blood products to Medicare beneficiaries); and (iv) maintaining software and data integration necessary for the reporting requirements described in paragraph (2)(A); and (B) be paid to participants as a lump sum on a monthly or quarterly basis. (4) Scope of model The Secretary shall implement the model in a manner that will provide for a sufficient number of participants in all HHS regions (as determined by the Secretary) and in varying types of geographic areas (including rural, frontier, suburban and urban) to assess and evaluate the reporting components required in the report under paragraph (5) . (5) Report Not later than 1 year after the termination of the model under this subsection, the Secretary shall submit to Congress a report that includes an analysis of the following: (A) Whether supplemental payments for ground and air ambulance services under the model under this subsection increased the utilization of blood and blood products and lessened the adverse effects of the specified medications in shortage. (B) The impact of providing such specified medications and blood products on the quality of care provided, and patient outcomes including Medicare and Medicaid patient morbidity and mortality. (C) Whether such increased utilization of specified medications and blood products improved the quality of care and saved lives for traditionally underserved demographics and rural communities. (6) Duration The model described in paragraph (1) shall be carried out for a period of not less than 5 years. (7) Definitions In this subsection: (A) Specified life-saving EMS medication The term specified life-saving EMS medication means the following drugs that have the meaning given the term life-saving in section 356(a)(1) of the Food, Drug and Cosmetic Act: (i) Epinephrine. (ii) Lidocaine. (iii) Calcium. (iv) 0.9 percent saline solution. (v) Lactated Ringers solution. (vi) Albuterol. (vii) Midazolam. (viii) 10 percent dextrose solution. (ix) Fentanyl. (B) Blood product The term blood product means any therapeutic substance derived from human blood, including whole blood and other blood components for transfusion, and plasma-derived medicinal products. (C) Eligible entity The term eligible entity means an emergency medical services agency (as defined in section 303(k)(13)(D) of the Controlled Substances Act). .\n#### 3. MedPAC report; EMTALA guidance\n##### (a) MedPAC report\n**(1) In general**\nNot later than 2 years after the date of the enactment of this Act, the Medicare Payment Advisory Commission (in this section referred to as MedPAC ) shall submit to Congress a report on payment for emergency medical services under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ). Such report shall include\u2014\n**(A)**\nwith respect to EMS medical directors, the evaluation described in paragraph (2) ;\n**(B)**\nwith respect to emergency medical services professionals, the evaluation described in paragraph (3) ;\n**(C)**\nwith respect to quality assurance, the recommendations described in paragraph (4) ; and\n**(D)**\nwith respect to emergency medical services, the analysis and recommendation described in paragraph (5) .\n**(2) EMS medical director evaluation**\n**(A) In general**\nFor purposes of paragraph (1)(A) , the evaluation described in this subsection is, with respect to EMS medical directors and the 1-year period preceding the date of the enactment of the When Minutes Count for Emergency Medical Patients Act, an evaluation of the key roles and responsibilities of physician medical directors in ensuring the highest quality of emergency medical services furnished to a Medicare beneficiary and shall include the following information:\n**(i)**\nAn analysis of the extent to which payment under title XVIII of the Social Security Act to emergency medical services agencies as providers or suppliers of ground and air ambulance services during such period was sufficient to enable such agencies to reimburse EMS medical directors for the roles and responsibilities of medical direction and oversight services identified by the sources of information in subparagraph (B) .\n**(ii)**\nConsider how modernization of EMS services that allows an emergency medical services agency that is an ambulance provider or supplier under title XVIII of the Social Security ( 42 U.S.C. 1395 et seq. ) to treat a patient in place and not transport the patient to a hospital, or to transport the patient to an appropriate clinical setting that is not a hospital, may increase the necessity and intensity of physician supervision to ensure patient safety and quality of care of patients with emergency medical conditions not being transported to a hospital.\n**(iii)**\nRecommendations as to potential models of payment under title XVIII of the Social Security Act for services furnished by EMS medical directors, including\u2014\n**(I)**\nany recommended difference in payment for online and offline medical direction; and\n**(II)**\nrecommendations as to whether separate payment under such title XVIII for medical direction and oversight would be justified to ensure high quality of emergency care provided to Medicare beneficiaries and how such separate payment could be implemented.\n**(B) Sources of information**\nIn conducting the evaluation under subparagraph (A) , MedPAC shall consider the following sources of information with respect to the role of EMS medical directors in the provision of emergency medical services:\n**(i)**\nThe official position statement with respect to EMS medical director compensation of the National Association of EMS Physicians.\n**(ii)**\nThe Health Resources and Services Administration Guide for Preparing Medical Directors.\n**(iii)**\nThe National Highway Traffic Safety Administration Guide for Preparing Medical Directors.\n**(iv)**\nThe United States Fire Administration Handbook for Medical Directors.\n**(v)**\nThe supervision requirements under section 303(k) of the Controlled Substances Act.\n**(vi)**\nThe Medicare Ground Ambulance Data Collection System established under section 1834(l)(17) of the Social Security Act ( 42 U.S.C. 1395m(l)(17) ).\n**(vii)**\nThe American College of Emergency Physicians policy statement entitled Physician Medical Direction of Emergency Medical Services Education Programs .\n**(viii)**\nAny other relevant information.\n**(3) Emergency medical services professional evaluation**\nFor purposes of paragraph (1)(B) , the evaluation described in this subsection is, with respect to emergency medical services professionals and the 1-year period preceding the date of the enactment of the When Minutes Count for Emergency Medical Patients Act, an evaluation of the key roles and responsibilities of emergency medical services professionals who provide care and treatment to Medicare beneficiaries, and shall include the following information:\n**(A)**\nAn analysis of the shortage of EMS professionals since 2020 and the impact of such shortage on access by Medicare beneficiaries to emergency medical services, including causes and potential solutions.\n**(B)**\nAn analysis of the extent to which payment under title XVIII of the Social Security Act impacts such shortage, and whether EMS agencies require additional payment under such title XVIII to attract and retain capable EMS professionals.\n**(C)**\nAn analysis of how modernization of EMS services described in paragraph (2)(A) may impact the staffing of professionals to provide such services.\n**(D)**\nRecommendations on any changes that should be made to ensure a sufficient and capable EMS professional workforce to provide the highest quality of care and transport for Medicare beneficiaries with emergency medical conditions.\n**(E)**\nAny other relevant information on the current and potential future role of such professionals in the provision of emergency medical services, community paramedicine, and mobile integrated health care services.\n**(4) Quality assurance recommendations**\nFor purposes of paragraph (1)(C) , the recommendations described in this subsection are recommendations with respect to mechanisms that may be used by Congress to ensure the highest quality of emergency medical services furnished to Medicare beneficiaries, such as the use of quality measures or conditions of participation under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ). In forming such recommendations, MedPAC shall take into consideration\u2014\n**(A)**\nthe uniqueness of the emergency medical services delivery model; and\n**(B)**\ndifferent types of emergency medical services agencies, as described in section 303(k)(13)(D) of the Controlled Substances Act ( 21 U.S.C. 823(k)(13)(D) ).\n**(5) Emergency medical services definition analysis and recommendation**\nFor purposes of paragraph (1)(D) , the analysis and recommendation described in this subsection are the following:\n**(A)**\nAn analysis of the consequences of amending section 1861 of the Social Security Act ( 42 U.S.C. 1395x ) to add a definition of the term emergency medical services that is consistent with the definition of such term in section 303(k)(13)(C) of the Controlled Substances Act ( 21 U.S.C. 823(k)(13)(C) ).\n**(B)**\nA recommendation as to whether the term provider of services under section 1861(u) of the Social Security Act ( 42 U.S.C. 1395x(u) ) should be amended to include an emergency medical services agency. Such recommendation shall include\u2014\n**(i)**\nan evaluation of any changes to payment under title XVIII of such Act that would result from such an amendment;\n**(ii)**\nan evaluation of any other potential benefits or obligations under titles XVIII and XIX of such Act that would result from such an amendment; and\n**(iii)**\nany other relevant information.\n##### (b) EMTALA guidance and report\n**(1) Guidance**\nNot later than 1 year after the date of enactment of this Act, the Secretary of Health and Human Services shall issue guidance to hospitals that have a hospital emergency department, regarding the obligation of such hospitals to address wall time pursuant to section 1867 of the Social Security Act ( 42 U.S.C. 1395dd ).\n**(2) Report**\nNot later than 1 year after the date on which the guidance is issued under paragraph (1) , the Secretary shall submit a report to Congress that includes an evaluation of whether such guidance has decreased the incidences of wall time during the such year, and any recommendations for legislation that the Secretary believes Congress should consider enacting to eliminate wall time.\n##### (c) Definitions\nIn this section, the following definitions apply:\n**(1) Emergency medical services**\nThe term emergency medical services \u2014\n**(A)**\nhas the meaning given such term in section 303(k)(13)(C) of the Controlled Substances Act ( 21 U.S.C. 823(k)(13)(C) ); and\n**(B)**\nincludes ambulance services (whether ground or air) covered under section 1834(l) of the Social Security Act ( 42 U.S.C. 1395m(l) ).\n**(2) Emergency medical services agency**\nThe term emergency medical services agency has the meaning given such term in section 303(k)(13)(D) of the Controlled Substances Act ( 21 U.S.C. 823(k)(13)(D) ).\n**(3) Emergency medical services professional**\nThe term emergency medical services professional has the meaning given such term in section 303(k)(13)(E) of the Controlled Substances Act ( 21 U.S.C. 823(k)(13)(E) ).\n**(4) EMS medical director**\nThe term EMS medical director has the meaning given the term medical director in section 303(k)(13)(H) of the Controlled Substances Act ( 21 U.S.C. 823(k)(13)(H) ).\n**(5) Medicare beneficiary**\nThe term Medicare beneficiary means an individual entitled to benefits under part A of title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ) or enrolled under part B of such title.\n**(6) Wall time**\nThe term wall time means the amount of time beyond 30 minutes of patient hand off from EMS professionals to hospital clinical personnel able to provide care to the patient at a hospital emergency department or freestanding emergency department.\n**(7) Specified drug**\nThe term specified drug has the meaning given the term specified life-saving EMS medication in section 1115A(h)(7) of the Social Security Act, as added by section 2 of the When Minutes Count for Emergency Medical Patients Act .",
      "versionDate": "2025-05-15",
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
        "name": "Health",
        "updateDate": "2025-09-17T15:02:33Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3443ih.xml"
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
      "title": "When Minutes Count for Emergency Medical Patients Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "When Minutes Count for Emergency Medical Patients Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XI of the Social Security Act to create a model, and to direct the Medicare Payment Advisory Commission to carry out a study and report with respect to Medicare payment for emergency medical services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T05:18:49Z"
    }
  ]
}
```
