# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6549?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6549
- Title: VA Contracting and Procurement Act
- Congress: 119
- Bill type: HR
- Bill number: 6549
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-05-21T08:08:41Z
- Update date including text: 2026-05-21T08:08:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-10 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-18 - Committee: Committee Hearings Held
- 2026-05-20 - Committee: Committee Hearings Held
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-10 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-18 - Committee: Committee Hearings Held
- 2026-05-20 - Committee: Committee Hearings Held

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6549",
    "number": "6549",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001301",
        "district": "1",
        "firstName": "Jack",
        "fullName": "Rep. Bergman, Jack [R-MI-1]",
        "lastName": "Bergman",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "VA Contracting and Procurement Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:41Z",
    "updateDateIncludingText": "2026-05-21T08:08:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Hearings Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
        "item": [
          {
            "date": "2026-05-20T13:25:44Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2026-03-18T16:45:29Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-12-10T15:03:15Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-10T15:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6549ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6549\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Bergman introduced the following bill; which was referred to the Committee on Veterans' Affairs , and in addition to the Committee on Rules , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 38, United States Code, to limit the obligation or expenditure of funds by the Secretary of Veterans Affairs for certain purposes.\n#### 1. Short title\nThis Act may be cited as the VA Contracting and Procurement Act .\n#### 2. Limitation on obligation or expenditure of funds by the Secretary of Veterans Affairs for certain purposes\n##### (a) Contracts and personal services\nSection 513 of title 38, United States Code, is amended\u2014\n**(1)**\nby inserting (a) In general.\u2014 before The Secretary ; and\n**(2)**\nby adding at the end the following new subsection:\n(b) Limitation on obligation or expenditure of funds (1) Subject to paragraph (2), the Secretary may not obligate or expend more than $50,000,000 for any contract or agreement under this section unless funds for such agreement have been specifically authorized by law. (2) The limitation under paragraph (1) shall not apply during\u2014 (A) a war declared by Congress; (B) a case described in section 4(a)(1) of the War Powers Resolution ( Public Law 93\u2013148 ; 50 U.S.C. 1543(a)(1) ); (C) a national emergency declared by the President under the National Emergencies Act ( Public Law 94\u2013412 ; 50 U.S.C. 1601 et seq. ); (D) a major disaster declared by the President under section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 ) if\u2014 (i) such agreement is to be carried out in a State affected by such major disaster; and (ii) a medical facility of the Department is affected by such major disaster; or (E) a public health emergency declared by the Secretary of Health and Human Services under section 319 of the Public Health Service Act ( 42 U.S.C. 247d ). .\n##### (b) Veterans Community Care Program\nSection 1703 of title 38, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (q) as subsection (r); and\n**(2)**\nby inserting after subsection (p) the following new subsection (q):\n(q) Limitation on obligation or expenditure of funds (1) Subject to paragraph (2), the Secretary may not obligate or expend more than $50,000,000 for any agreement under this section unless funds for such agreement have been specifically authorized by law. (2) The limitation under paragraph (1) shall not apply during\u2014 (A) a war declared by Congress; (B) a case described in section 4(a)(1) of the War Powers Resolution ( Public Law 93\u2013148 ; 50 U.S.C. 1543(a)(1) ); (C) a national emergency declared by the President under the National Emergencies Act ( Public Law 94\u2013412 ; 50 U.S.C. 1601 et seq. ); (D) a major disaster declared by the President under section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 ) if\u2014 (i) such agreement is to be carried out in a State affected by such major disaster; and (ii) a medical facility of the Department is affected by such major disaster; or (E) a public health emergency declared by the Secretary of Health and Human Services under section 319 of the Public Health Service Act ( 42 U.S.C. 247d ). .\n##### (c) Agreements To administer the furnishing of health care in Department facilities\nSection 1721 of title 38, United States Code, is amended\u2014\n**(1)**\nin the section heading, by adding and to enter into agreements after regulations (and conforming the table of sections at the beginning of such chapter accordingly);\n**(2)**\nby inserting (a) Rules and regulations.\u2014 before Rules and regulations ; and\n**(3)**\nby adding at the end the following new subsection:\n(b) Agreements (1) The Secretary may enter into an agreement (including an agreement regarding information technology) to administer the furnishing of care described in subsection (a). (2) Subject to paragraph (2), the Secretary may not obligate or expend more than $50,000,000 for any agreement under this section unless funds for such agreement have been specifically authorized by law. (3) The limitation under paragraph (2) shall not apply during\u2014 (A) a war declared by Congress; (B) a case described in section 4(a)(1) of the War Powers Resolution ( Public Law 93\u2013148 ; 50 U.S.C. 1543(a)(1) ); (C) a national emergency declared by the President under the National Emergencies Act ( Public Law 94\u2013412 ; 50 U.S.C. 1601 et seq. ); (D) a major disaster declared by the President under section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 ) if\u2014 (i) such agreement is to be carried out in a State affected by such major disaster; and (ii) a medical facility of the Department is affected by such major disaster; or (E) a public health emergency declared by the Secretary of Health and Human Services under section 319 of the Public Health Service Act ( 42 U.S.C. 247d ). .\n##### (d) Administration of educational benefits\nSubchapter III of chapter 36 of title 38, United States Code, is amended by inserting after section 3698A the following new section (and conforming the table of sections at the beginning of such chapter accordingly):\n3698B. Limitation on obligation or expenditure of funds (a) Limitation The Secretary may not obligate or expend more than $50,000,000 for any agreement under this chapter unless\u2014 (1) funds for such agreement have been specifically authorized by law; or (2) (A) the Secretary has submitted a notification described in subsection (b) regarding such agreement; (B) 30 legislative days have elapsed after the date of such submission; and (C) Congress has not enacted a joint resolution described in subsection (c) regarding such agreement. (b) Notification (1) A notification described in this subsection is a notification\u2014 (A) submitted by the Secretary to the Committees on Veterans\u2019 Affairs of the Senate and the House of Representatives; and (B) that describes a proposed agreement subject to the limitation under subsection (a). (2) A notification under this subsection shall include the following with respect to such proposed agreement: (A) The purpose. (B) The scope. (C) The estimated total cost. (D) The anticipated period of performance. (c) Joint resolution A joint resolution of disapproval described in this subsection is a joint resolution\u2014 (1) introduced not later than 10 legislative days after receipt of a notification under subsection (b); (2) the matter after the resolving clause of which is as follows: That Congress disapproves the proposed agreement described by the Secretary of Veterans Affairs in the notification submitted under section 3698B of title 38, United States Code, on ____________________. , the blank space being filled with the appropriate date; and (3) considered pursuant to the expedited procedures in subsections (d), (f), and (g) of section 802 of title 5. .\n##### (e) Administration of benefits\nChapter 53 of title 38, United States Code, is amended by adding at the end the following new section (and conforming the table of sections at the beginning of such chapter accordingly):\n5322. Limitation on obligation or expenditure of funds (a) Limitation Subject to subsection (b), the Secretary may not obligate or expend more than $50,000,000 for any agreement under this chapter unless funds for such agreement have been specifically authorized by law. (b) Applicability The limitation under subsection (a) shall not apply during\u2014 (1) a war declared by Congress; (2) a case described in section 4(a)(1) of the War Powers Resolution ( Public Law 93\u2013148 ; 50 U.S.C. 1543(a)(1) ); (3) a national emergency declared by the President under the National Emergencies Act ( Public Law 94\u2013412 ; 50 U.S.C. 1601 et seq. ); (4) a major disaster declared by the President under section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 ) if\u2014 (A) such agreement is to be carried out in a State affected by such major disaster; and (B) a medical facility of the Department is affected by such major disaster; or (5) a public health emergency declared by the Secretary of Health and Human Services under section 319 of the Public Health Service Act ( 42 U.S.C. 247d ). .\n##### (f) Procurement of health-Care items\nSection 8127 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (c), by striking subsection (a) or (b) and inserting subsection (a), (b), or (c) ;\n**(2)**\nin subsection (d), by adding at the end the following new paragraph:\n(4) The term domestic preference statute has the meaning given such term in section 70923(f) of the Infrastructure Investment and Jobs Act ( Public Law 117\u201358 ; 41 U.S.C. 8301 note). ;\n**(3)**\nby redesignating subsections (c) and (d), as amended, as subsections (d) and (e), respectively; and\n**(4)**\nby inserting after subsection (b) the following new subsection (c):\n(c) (1) The Secretary shall procure a health-care item for an All-Hazards Emergency Cache of the Department in compliance with the domestic preference statutes. (2) The limitation under paragraph (1) shall not apply if, during an emergency, the Secretary determines that procurement in compliance with the domestic preference statutes would threaten the health or safety of veterans. (3) Not later than 30 days after procuring a health-care item pursuant to paragraph (2), the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives a written notice. Such notice shall include\u2014 (A) an identification of the emergency; (B) an identification of the health-care item procured; (C) an estimate of the cost of such procurement; and (D) an explanation why the Secretary could not procure the health-care item in compliance with the domestic preference statutes. (4) Not later than November 1 of each year, the Secretary shall certify to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives whether the Secretary complied with the limitation under paragraph (1) during the fiscal year that ended most recently. .\n##### (g) Small business concerns owned and controlled by veterans: contracting goals and preferences\nSection 8127 of title 38, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (m) as subsection (n); and\n**(2)**\nby inserting after subsection (l) the following new subsection (m):\n(m) Limitation on obligation or expenditure of funds (1) Subject to paragraph (2), the Secretary may not obligate or expend more than $50,000,000 for any agreement under this section unless funds for such agreement have been specifically authorized by law. (2) The limitation under paragraph (1) shall not apply during\u2014 (A) a war declared by Congress; (B) a case described in section 4(a)(1) of the War Powers Resolution ( Public Law 93\u2013148 ; 50 U.S.C. 1543(a)(1) ); (C) a national emergency declared by the President under the National Emergencies Act ( Public Law 94\u2013412 ; 50 U.S.C. 1601 et seq. ); (D) a major disaster declared by the President under section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 ) if\u2014 (i) such agreement is to be carried out in a State affected by such major disaster; and (ii) a medical facility of the Department is affected by such major disaster; or (E) a public health emergency declared by the Secretary of Health and Human Services under section 319 of the Public Health Service Act ( 42 U.S.C. 247d ). .\n##### (h) Sharing of health-Care resources\nSection 8153 of title 38, United States Code, is amended by adding at the end the following new subsection:\n(h) (1) Subject to paragraph (2), the Secretary may not obligate or expend more than $50,000,000 for any agreement under this section unless funds for such agreement have been specifically authorized by law. (2) The limitation under paragraph (1) shall not apply during\u2014 (A) a war declared by Congress; (B) a case described in section 4(a)(1) of the War Powers Resolution ( Public Law 93\u2013148 ; 50 U.S.C. 1543(a)(1) ); (C) a national emergency declared by the President under the National Emergencies Act ( Public Law 94\u2013412 ; 50 U.S.C. 1601 et seq. ); (D) a major disaster declared by the President under section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 ) if\u2014 (i) such agreement is to be carried out in a State affected by such major disaster; and (ii) a medical facility of the Department is affected by such major disaster; or (E) a public health emergency declared by the Secretary of Health and Human Services under section 319 of the Public Health Service Act ( 42 U.S.C. 247d ). .\n#### 3. Procurement of prosthetic appliances and surgical implants\n##### (a) In general\nSection 8123 of title 38, United States Code, is amended to read as follows (and the table of sections at the beginning of chapter 81 of such title is amended accordingly):\n8123. Procurement of prosthetic appliances and surgical implants (a) Authority The Secretary may procure prosthetic appliances and surgical implants by purchase, manufacture, contract, or in such other manner that the Secretary determines to be proper. (b) Catalog (1) The Secretary shall maintain a catalog of prosthetic appliances and surgical implants that the Secretary procures by purchase or contract. (2) The Secretary shall coordinate with the Secretary of Defense to ensure that such catalog requires the same data regarding a prosthetic appliance or surgical implant that is required by the Defense Health Agency. (3) The Secretary shall implement a process by which a manufacturer of a prosthetic appliance or surgical implant may propose to the Secretary a proposed revision to such catalog (including with regards to form, size, generation, or model)\u2014 (A) by standardized and electronic means; (B) that minimizes the documentation required by such a manufacturer. (c) Purchase orders for surgical implants The Secretary shall procure all surgical implants used in a medical procedure through\u2014 (1) a firm-fixed price single purchase order submitted and processed through the Prosthetic and Sensory Aids Service of the Department; (2) in accordance with the Federal Acquisition Regulation; and (3) a process that\u2014 (A) eliminates duplicative billing; and (B) allows the Secretary to correct errors in real time. (d) Definitions In this section: (1) The term Federal Acquisition Regulation means the Federal Acquisition Regulation issued pursuant to section 1303(a)(1) of title 41. (2) The term firm-fixed price has the meaning given such term in the Federal Acquisition Regulation. (3) The term prosthetic appliance includes any service or product required in the fitting, supplying, training, or use of a prosthetic appliance. (4) The term surgical implant includes any item used in a surgery regarding a surgical implant, including an implantable device, a screw, guidewire, or surgical tool. .\n##### (b) Implementation\nThe Secretary of Veterans Affairs shall implement\u2014\n**(1)**\nsubsection (c) of such section, as added by this section, not later than one year after the date of the enactment of this Act; and\n**(2)**\nsubsection (b) of such section, as added by this section, not later than three years after the date of the enactment of this Act. Until the Secretary implements such subsection, the Secretary shall accept a proposed revision described in such subsection during at least two periods, prescribed by the Secretary, per year.",
      "versionDate": "2025-12-10",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-07T23:20:07Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6549ih.xml"
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
      "title": "VA Contracting and Procurement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-27T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VA Contracting and Procurement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-27T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to limit the obligation or expenditure of funds by the Secretary of Veterans Affairs for certain purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-27T05:33:26Z"
    }
  ]
}
```
