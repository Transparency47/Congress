# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8119?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8119
- Title: HOPE with Fertility Services Act
- Congress: 119
- Bill type: HR
- Bill number: 8119
- Origin chamber: House
- Introduced date: 2026-03-26
- Update date: 2026-04-28T08:06:36Z
- Update date including text: 2026-04-28T08:06:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-03-26: Introduced in House

## Actions

- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8119",
    "number": "8119",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "HOPE with Fertility Services Act",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:36Z",
    "updateDateIncludingText": "2026-04-28T08:06:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T14:05:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "FL"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "NY"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "PA"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "FL"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NJ"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "NY"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NY"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "CA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NY"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "WI"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "OH"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "PA"
    },
    {
      "bioguideId": "C001051",
      "district": "31",
      "firstName": "John",
      "fullName": "Rep. Carter, John R. [R-TX-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "TX"
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
      "sponsorshipDate": "2026-04-15",
      "state": "DC"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "NY"
    },
    {
      "bioguideId": "K000401",
      "district": "3",
      "firstName": "Kevin",
      "fullName": "Rep. Kiley, Kevin [I-CA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiley",
      "party": "I",
      "sponsorshipDate": "2026-04-20",
      "state": "CA"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "MI"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8119ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8119\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2026 Mr. Nunn of Iowa (for himself, Ms. Wasserman Schultz , Ms. Malliotakis , Ms. Houlahan , Ms. Lee of Florida , Mr. Norcross , Mr. Lawler , Mr. Ryan , Mrs. Kim , Mr. Goldman of New York , Mr. Van Orden , Mr. Landsman , and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo ensure coverage for the treatment of infertility for certain conditions.\n#### 1. Short title\nThis Act may be cited as the Helping to Optimize Patients\u2019 Experience with Fertility Services Act or the HOPE with Fertility Services Act .\n#### 2. ensuring benefits for treatment of infertility and iatrogenic infertility\n##### (a) In general\nSubpart B of part 7 of subtitle B of title I of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1185 et seq. ) is amended by inserting after section 714 the following:\n714A. Standards relating to benefits for treatment of infertility and iatrogenic infertility (a) In general A group health plan or a health insurance issuer offering group health insurance coverage shall ensure that such plan or coverage provides coverage for infertility or iatrogenic infertility treatments, including\u2014 (1) the treatment of infertility, if such plan or coverage provides coverage for obstetrical services; and (2) standard fertility preservation services when a medically necessary treatment described in subparagraph (A), (B), (C), or (D) of subsection (b)(1) causes, or is expected to cause, iatrogenic infertility. (b) Definitions In this section: (1) Iatrogenic infertility The term iatrogenic infertility means an impairment of fertility due to damage of reproductive organs and processes resulting from\u2014 (A) a surgical or other invasive medical procedure as a result of an injury or life-threatening illness, or involving a reproductive organ or process in a manner likely to cause damage to such organ or process; (B) radiation therapy; (C) chemotherapy; or (D) myeloablative conditioning. (2) Infertility The term infertility means a disease or condition characterized by\u2014 (A) the inability to achieve spontaneous pregnancy without medical treatment after a period of at least 12 consecutive months of unprotected sexual intercourse; (B) the inability to achieve pregnancy after receiving standard clinical treatment protocols under the supervision of a treating physician who is a board-certified reproductive endocrinologist or obstetrician-gynecologist; (C) being incapable of reproduction to live birth based on medical and reproductive history, age, physical findings or diagnostic testing of the individual, as determined by a treating physician; or (D) the inability to achieve spontaneous pregnancy on account of a diagnosed condition that is a disorder of ovulation, or a testicular or hormonal disease or disorder. (3) Infertility or iatrogenic infertility treatment The term infertility or iatrogenic infertility treatment means treatments or procedures with the intent of facilitating a pregnancy, including\u2014 (A) such treatments or procedures that involve the handling of human egg, sperm, and embryo outside of the body, including in vitro fertilization and maturation, egg and embryo cryopreservation, egg and embryo donation, and intracytoplasmic sperm injection; or (B) such treatments or procedures that do not involve the handling of human egg, sperm, and embryo outside of the body, including ovulation induction, genetic screening and diagnosis, sperm cryopreservation, and intrauterine insemination. (c) Required coverage A group health plan and a health insurance issuer offering group health insurance coverage that includes coverage for obstetrical services shall provide comprehensive coverage for infertility or iatrogenic infertility treatments, as determined by the Secretary in consultation with relevant stakeholders, provided to a participant or beneficiary if\u2014 (1) the participant or beneficiary has infertility, including iatrogenic infertility; and (2) the treatment or service is performed at a medical facility that is in compliance with standards set by appropriate Federal and State agencies. (d) Financial requirements and treatment requirements Any coverage provided by a group health plan or health insurance issuer in accordance with this section may be subject to coverage limits (such as medical necessity, pre-authorization, or pre-certification) and cost-sharing requirements (such as coinsurance, copayments, and deductibles), as required under the group health plan or health insurance coverage, that are no more restrictive than the predominant coverage limits and cost-sharing requirements applied to substantially all medical and surgical benefits covered under the plan or coverage. (e) Prohibitions A group health plan and a health insurance issuer offering group health insurance coverage may not\u2014 (1) provide incentives (monetary or otherwise) to a participant or beneficiary to encourage such participant or beneficiary not to be provided infertility or iatrogenic infertility treatments to which such participant or beneficiary is entitled under this section, or to providers to induce such providers not to provide such treatments to qualified participants and beneficiaries; (2) prohibit a provider from discussing with a participant or beneficiary infertility or iatrogenic infertility treatments or medical treatment options required to be covered under this section; or (3) penalize or otherwise reduce or limit the reimbursement of a provider because such provider provided infertility or iatrogenic infertility treatment services to a participant or beneficiary in accordance with this section. (f) Rule of construction Nothing in this section shall be construed to\u2014 (1) require a participant or beneficiary in a group health plan or group health insurance coverage to undergo infertility or iatrogenic infertility treatments; (2) impact the use by a group health plan or a health insurance issuer offering group health insurance coverage of utilization management tools; or (3) prevent a group health plan or a health insurance issuer offering group health insurance coverage from contracting with providers as to the level and type of reimbursement with a provider for care provided in accordance with this section. (g) Utilization management tools requirements (1) In general In the case of a group health plan or a health insurance issuer offering group health insurance coverage that imposes utilization management tools on infertility and iatrogenic infertility treatment benefits, for the first 5 plan years that begin after the date of enactment of the Helping to Optimize Patients\u2019 Experience with Fertility Services Act, such plan or issuer shall perform and document analyses of the design and application of the utilization management tool such analysis and the following information: (A) The specific plan or coverage terms or other relevant terms regarding the utilization management tools and a description of all infertility or iatrogenic infertility treatment benefits, to which each such term applies in each respective benefits classification. (B) The factors used to determine that the utilization management tool will apply to infertility or iatrogenic infertility treatment benefits. (C) The evidentiary standards used for the factors identified under subparagraph (B), when applicable, provided that every factor shall be defined, and any other source or evidence relied upon to design and apply the utilization management tool to infertility and iatrogenic infertility treatment benefits. (D) An analysis demonstrating that the processes, strategies, evidentiary standards, and other factors used to apply the utilization management tools to infertility and iatrogenic infertility treatment benefits as written and in operation, are consistent with, and are applied no more stringently than with clinical guidelines for infertility or iatrogenic infertility treatments. (E) The specific findings and conclusions reached by the group health plan or health insurance issuer with respect to the health insurance coverage, including any results of the analyses described in this paragraph that indicate that the plan or coverage is or is not in compliance with this section. (2) Submission process (A) Annual submission A group health plan or health insurance issuer offering group health insurance coverage shall submit to the Secretary the analyses described in paragraph (1) annually for first 5 plan years that begin after the date of enactment of the Helping to Optimize Patients\u2019 Experience with Fertility Services Act. For subsequent plan years, the Secretary may request that a group health plan or a health insurance issuer offering group health insurance coverage submit the analysis described in paragraph (1) in the case of potential violations of this section or complaints regarding noncompliance with this section that concern utilization management tools and any other instances in which the Secretary determines appropriate. (B) Additional information If the Secretary concludes that a group health plan or health insurance issuer has not submitted sufficient information for the Secretary to review the analysis described in paragraph (1), the Secretary shall specify to the plan or issuer the information the plan or issuer is required to submit pursuant to subparagraph (A). Nothing in this subparagraph shall require the Secretary to conclude that a group health plan or health insurance issuer is in compliance with this section solely based upon the inspection of the analyses described in paragraph (1), as requested under subparagraph (A). (3) Required action (A) In general If, after review of the analyses described in paragraph (1), the Secretary notifies the group health plan or health insurance issuer that such plan or issuer is not in compliance with this section, the plan or issuer\u2014 (i) shall specify to the Secretary the actions the plan or issuer will take to be in compliance with this section and provide to the Secretary additional analyses described in paragraph (1) that demonstrate compliance with this section not later than 45 days after the initial notification by the Secretary that the plan or issuer is not in compliance; and (ii) following the 45-day corrective action period under clause (i), if the Secretary makes a final determination that the plan or issuer still is not in compliance with this section, not later than 7 days after such determination, shall notify all individuals enrolled in the applicable plan or health insurance coverage that such plan or coverage has been determined to be not in compliance with this section. (B) Exemption from disclosure Documents or communications produced in connection with the Secretary\u2019s recommendations to a group health plan or health insurance issuer shall not be subject to disclosure pursuant to section 552 of title 5, United States Code. (4) Report For plan years beginning on or after January 1, 2027, the Secretary shall submit to Congress, and make publicly available, a report that contains\u2014 (A) a summary of the analysis submitted under paragraph (1), including the identity of each group health plan or health insurance issuer offering health insurance coverage that is determined to be not in compliance after the final determination by the Secretary described in paragraph (3)(A)(ii); (B) the Secretary\u2019s conclusions as to whether each group health plan or health insurance issuer submitted sufficient information for the Secretary to review the analysis under paragraph (2); (C) for each group health plan or health insurance issuer that did submit sufficient information under paragraph (2), the Secretary\u2019s conclusions as to whether and why the plan or issuer is in compliance with the requirements under this section; (D) the Secretary\u2019s specifications described in paragraph (3) for each group health plan or health insurance issuer that the Secretary determined did not submit sufficient information for the Secretary to review the analyses described in paragraph (1) for compliance with this section; and (E) the actions the Secretary specifies under paragraph (3)(A)(i) that each group health plan or health insurance issuer that the Secretary determined is not in compliance with this section is required take to be in compliance with this section, including the reason why the Secretary determined the plan or issuer is not in compliance. (h) Notice Beginning with the second plan year beginning after the date of enactment of the Helping to Optimize Patients\u2019 Experience with Fertility Services Act, a group health plan and a health insurance issuer offering group health insurance coverage shall provide notice to participants and beneficiaries in such plan or coverage regarding the coverage required by this section in accordance with regulations promulgated by the Secretary. (i) Effective date This section, and the amendments made by this section, shall apply with respect to plan years beginning on or after January 1, 2027. .\n##### (b) Enforcement\nSection 502 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1132 ) is amended\u2014\n**(1)**\nin subsection (a)(6), by striking or (9) and inserting (9), or (13) ;\n**(2)**\nin subsection (b)(3), by striking subsection (c)(9) and inserting paragraphs (9) and (13) of subsection (c) ; and\n**(3)**\nin subsection (c), by adding at the end the following:\n(13) (A) The Secretary may assess a civil penalty against a health insurance issuer for failing to provide coverage for infertility or iatrogenic infertility treatments as required under section 714A, in an amount up to $100 per day, beginning on the date on which the issuer first denies such coverage and ending on the date on which the issuer approves coverage, with respect to each participant or beneficiary denied such coverage in violation of such section. (B) The Secretary may assess a civil penalty against a health insurance issuer for failing to submit an analysis as required under section 714A(g)(2), in an amount up to $100 for each day, beginning 45 days after the date on which the Secretary notifies such issuer that the issuer is not in compliance with the requirement under section 714A(g)(2), and ending on the date on which the issue submits the analysis as required. .\n##### (c) Conforming amendment\nSection 731(c) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1191(c) ) is amended by striking section 711 and inserting sections 711 and 714A .",
      "versionDate": "2026-03-26",
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
        "updateDate": "2026-04-14T19:42:23Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8119ih.xml"
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
      "title": "HOPE with Fertility Services Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-11T03:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HOPE with Fertility Services Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-11T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Helping to Optimize Patients\u2019 Experience with Fertility Services Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-11T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure coverage for the treatment of infertility for certain conditions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-11T03:48:31Z"
    }
  ]
}
```
