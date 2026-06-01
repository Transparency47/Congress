# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3228?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3228
- Title: SIMSA Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3228
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2025-12-02T14:58:46Z
- Update date including text: 2025-12-02T14:58:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3228",
    "number": "3228",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "SIMSA Act of 2025",
    "type": "S",
    "updateDate": "2025-12-02T14:58:46Z",
    "updateDateIncludingText": "2025-12-02T14:58:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T16:43:58Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NH"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "IA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NH"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3228is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3228\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mr. Grassley (for himself, Ms. Hassan , Ms. Ernst , Mrs. Shaheen , and Mrs. Capito ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Controlled Substances Act to clarify how controlled substance analogues that are imported or offered for import are to be regulated, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Stop the Importation and Manufacturing of Synthetic Analogues Act of 2025 or the SIMSA Act of 2025 .\n##### (b) Table of contents\nThe table of contents of this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Establishment of Schedule A.\nSec. 3. Temporary and permanent scheduling of schedule A substances.\nSec. 4. Penalties.\nSec. 5. False labeling of schedule A controlled substances.\nSec. 6. Registration requirements for schedule A substances.\nSec. 7. Additional conforming amendments.\nSec. 8. Sentencing review.\nSec. 9. Rules of construction.\n#### 2. Establishment of Schedule A\nSection 202 of the Controlled Substances Act ( 21 U.S.C. 812 ) is amended\u2014\n**(1)**\nin subsection (a), by striking five schedules of controlled substances, to be known as schedules I, II, III, IV, and V and inserting six schedules of controlled substances, to be known as schedules I, II, III, IV, V, and A ;\n**(2)**\nin subsection (b), by adding at the end the following:\n(6) Schedule A (A) In general The drug or substance\u2014 (i) is or has been imported, or is offered for import, into the United States; (ii) has\u2014 (I) a chemical structure that is substantially similar to the chemical structure of a controlled substance in schedule I, II, III, IV, or V; and (II) an actual or predicted stimulant, depressant, or hallucinogenic effect on the central nervous system that is substantially similar to or greater than the stimulant, depressant, or hallucinogenic effect on the central nervous system of a controlled substance in schedule I, II, III, IV, or V; and (iii) is not listed or otherwise included in any other schedule in this section or by regulation of the Attorney General. (B) Predicted stimulant, depressant, or hallucinogenic effect For purpose of this paragraph, a predicted stimulant, depressant, or hallucinogenic effect on the central nervous system may be based on\u2014 (i) (I) the chemical structure; and (II) (aa) the structure activity relationships; or (bb) binding receptor assays and other relevant scientific information about the substance; (ii) (I) the current or relative potential for abuse of the substance; and (II) the clandestine importation, manufacture, or distribution, or diversion from legitimate channels, of the substance; or (iii) the capacity of the substance to cause a state of dependence, including physical or psychological dependence that is similar to or greater than that of a controlled substance in schedule I, II, III, IV, or V. ; and\n**(3)**\nin subsection (c)\u2014\n**(A)**\nin the matter preceding schedule I, by striking IV, and V and inserting IV, V, and A ; and\n**(B)**\nby adding at the end the following:\nSchedule A Any substance temporarily or permanently scheduled by the Attorney General in accordance with section 201(k). .\n#### 3. Temporary and permanent scheduling of schedule A substances\nSection 201 of the Controlled Substances Act ( 21 U.S.C. 811 ) is amended by adding at the end the following:\n(k) Temporary and permanent scheduling of schedule A substances (1) In general The Attorney General may issue a temporary order adding a drug or substance to schedule A if the Attorney General finds that\u2014 (A) the drug or other substance satisfies the criteria for being considered a schedule A substance; and (B) adding such drug or substance to schedule A will assist in preventing abuse of the drug or other substance. (2) Duration of temporary scheduling order A temporary scheduling order issued under paragraph (1) shall\u2014 (A) not take effect until 30 days after the date of the publication by the Attorney General of a notice in the Federal Register of the intention to issue such order and the grounds upon which such order is to be issued; and (B) expire not later than 5 years after the date on which the order becomes effective, except that the Attorney General may, during the pendency of proceedings under paragraph (5), extend the temporary scheduling order for up to 180 days. (3) Effect of issuance of permanent scheduling order A temporary scheduling order issued under paragraph (1) shall be vacated upon the issuance of a permanent order issued under paragraph (5) with regard to the same substance, or upon the subsequent issuance of any scheduling order under this section. (4) Limitation on judicial review A temporary scheduling order issued under paragraph (1) shall not be subject to judicial review. (5) Permanent scheduling order (A) In general Except as provided in subparagraph (B), not earlier than 3 years after the date on which the Attorney General issues an order temporarily scheduling a drug or substance under this subsection, the Attorney General may, by rule, issue a permanent order adding the drug or other substance to schedule A if such drug or substance satisfies the criteria for being considered a schedule A substance. (B) Limitation If the Secretary of Health and Human Services, in consultation with the Attorney General, has determined, based on relevant scientific studies and necessary data gathered by the Secretary of Health and Human Services and gathered by the Attorney General, that a drug or other substance that has been temporarily placed in schedule A does not have sufficient potential for abuse to warrant control in any schedule, and provides a 30-day written notice of such determination to the Attorney General, the Attorney General\u2014 (i) may not issue a permanent scheduling order under subparagraph (A); and (ii) not later than 30 days after the date on which the Attorney General receives such notice, shall issue an order immediately terminating the temporary scheduling order for the drug or other substance. (6) Notice to HHS Before initiating proceedings under paragraph (1), the Attorney General shall transmit notice of a temporary order proposed to be issued to the Secretary of Health and Human Services. In issuing an order under paragraph (1), the Attorney General shall take into consideration any comments submitted by the Secretary of Health and Human Services in response to a notice transmitted pursuant to this paragraph. .\n#### 4. Penalties\nSection 1010 of the Controlled Substances Import and Export Act ( 21 U.S.C. 960 ) is amended\u2014\n**(1)**\nin subsection (a), by inserting or a drug or substance in schedule A after controlled substance each place it appears; and\n**(2)**\nin subsection (b), by adding at the end the following:\n(8) In the case of a violation under subsection (a) involving a controlled substance in schedule A, the person committing such violation shall be sentenced to a term of imprisonment of not more than 20 years and if death or serious bodily injury results from the use of such substance shall be sentenced to a term of imprisonment for any term of years or for life, a fine not to exceed the greater of that authorized in accordance with the provisions of title 18, United States Code, or $1,000,000 if the defendant is an individual or $5,000,000 if the defendant is other than an individual, or both. If any person commits such a violation after a prior conviction for a felony drug offense has become final, such person shall be sentenced to a term of imprisonment of not more than 30 years and if death or serious bodily injury results from the use of such substance shall be sentenced to a term of imprisonment for any term of years or for life, a fine not to exceed the greater of twice that authorized in accordance with the provisions of title 18, United States Code, or $2,000,000 if the defendant is an individual or $10,000,000 if the defendant is other than an individual, or both. Notwithstanding section 3583 of title 18, United States Code, any sentence imposing a term of imprisonment under this paragraph shall, in the absence of such a prior conviction, impose a term of supervised release of not less than 3 years in addition to such term of imprisonment and shall, if there was such a prior conviction, impose a term of supervised release of not less than 6 years in addition to such term of imprisonment. Notwithstanding the prior sentence, and notwithstanding any other provision of law, the court shall not place on probation or suspend the sentence of any person sentenced under the provisions of this paragraph which provide for a mandatory term of imprisonment if death or serious bodily injury results. .\n#### 5. False labeling of schedule A controlled substances\n##### (a) In general\nSection 305 of the Controlled Substances Act ( 21 U.S.C. 825 ) is amended by adding at the end the following:\n(f) False labeling of schedule A controlled substances (1) It shall be unlawful to import or export, with intent to manufacture, distribute, or dispense, a schedule A substance or product containing a schedule A substance, unless the substance or product bears a label clearly identifying a schedule A substance or product containing a schedule A substance by the nomenclature used by the International Union of Pure and Applied Chemistry (IUPAC). (2) (A) A product described in subparagraph (B) is exempt from the International Union of Pure and Applied Chemistry nomenclature requirement of this subsection if such product is labeled in the manner required under the Federal Food, Drug, and Cosmetic Act. (B) A product is described in this subparagraph if the product\u2014 (i) is the subject of an approved application as described in section 505(b) or (j) of the Federal Food, Drug, and Cosmetic Act; or (ii) is exempt from the provisions of section 505 of such Act relating to new drugs because\u2014 (I) it is intended solely for investigational use as described in section 505(i) of such Act; and (II) such product is being used exclusively for purposes of a clinical trial that is the subject of an effective investigational new drug application. .\n##### (b) Penalties\nSection 402 of the Controlled Substances Act ( 21 U.S.C. 842 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (16), by striking or at the end;\n**(B)**\nby redesignating paragraph (17) as paragraph (18); and\n**(C)**\nby inserting after paragraph (16) the following:\n(17) to violate section 305(f); or ; and\n**(2)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (B)(i), by striking (17) and inserting (18) ; and\n**(ii)**\nin subparagraph (C), by inserting or (17) after paragraph (16) each place it appears; and\n**(B)**\nin paragraph (2)(D), by striking (17) and inserting (18) .\n#### 6. Registration requirements for schedule A substances\n##### (a) Registration requirements for importers and exporters of schedule A substances\nSection 1008 of the Controlled Substances Import and Export Act ( 21 U.S.C. 958 ) is amended by adding at the end the following:\n(j) (1) The Attorney General shall register an applicant to import or export a schedule A substance if\u2014 (A) the applicant demonstrates that the schedule A substance will be used for research, analytical, or industrial purposes approved by the Attorney General; and (B) the Attorney General determines that such registration is consistent with the public interest and with the United States obligations under international treaties, conventions, or protocols in effect on the date of enactment of this subsection. (2) In determining the public interest under paragraph (1)(B), the Attorney General shall consider\u2014 (A) maintenance of effective controls against diversion of particular controlled substances and any controlled substance in schedule A compounded therefrom into other than legitimate medical, scientific, research, or industrial channels, by limiting the importation and bulk manufacture of such controlled substances to a number of establishments which can produce an adequate and uninterrupted supply of these substances under adequately competitive conditions for legitimate medical, scientific, research, and industrial purposes; (B) compliance with applicable State and local law; (C) promotion of technical advances in the art of manufacturing substances described in subparagraph (A) and the development of new substances; (D) prior conviction record of applicant under Federal and State laws relating to the importation, manufacture, distribution, or dispensing of substances described in subparagraph (A); (E) past experience in the importation and manufacture of controlled substances, and the existence in the establishment of effective control against diversion; and (F) such other factors as may be relevant to and consistent with the public health and safety. (3) If an applicant is registered to import or export a controlled substance in schedule I or II under subsection (a), the applicant shall not be required to apply for a separate registration under this subsection. .\n##### (b) Research on substances newly added to schedule A\nSection 302(e) of the Controlled Substances Act ( 21 U.S.C. 822(e) ) is amended by adding at the end the following:\n(3) (A) If a person is conducting research on a substance at the time the substance is added to schedule A, and such person, subject to an exemption that is in effect for investigational use, for that person, under section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) to the extent conduct with respect to such substance is pursuant to such exemption. .\n##### (c) Continuation of research on substances newly added to schedule A\nSection 302(e) of the Controlled Substances Act ( 21 U.S.C. 822(e) ), as amended by subsection (b) of this section, is amended by adding at the end the following:\n(B) If a person is conducting research on a substance at the time the substance is added to schedule A, and such person is already registered to conduct research with a controlled substance in schedule I or II, then\u2014 (i) the person shall, within 30 days of the scheduling of the newly-scheduled substance, submit a completed application for registration or modification of existing registration, to conduct research on such substance, in accordance with the regulations issued by the Attorney General; (ii) the person may continue to conduct the research on such substance until the application described in clause (i) is withdrawn by the applicant or until the Attorney General serves on the applicant an order to show cause proposing the denial of the application pursuant to section 304(c); and (iii) if the Attorney General serves order to show cause under clause (ii) and the applicant requests a hearing, such hearing shall be held on an expedited basis and not later than 45 days after the request is made, except that the hearing may be held at a later time if so requested by the applicant. (C) A person who is registered to conduct research with a controlled substance in schedule A may conduct research with another controlled substance in schedule I, only if\u2014 (i) the person has applied for a modification of the person's registration to authorize research with such other controlled substance in accordance with the regulations issued by the Attorney General; (ii) the Attorney General has obtained verification from the Secretary that the research protocol submitted with the application is meritorious; and (iii) the Attorney General has determined, not later than 30 days after receiving the application described in clause (i), that such activity is consistent with United States obligations under the Single Convention on Narcotic Drugs, 1961. (D) Nothing in this paragraph shall be construed to alter the authority of the Attorney General to initiate proceedings to deny, suspend, or revoke any registration in accordance with sections 303 and 304. .\n#### 7. Additional conforming amendments\nThe Controlled Substances Import and Export Act ( 21 U.S.C. 951 et seq. ) is amended\u2014\n**(1)**\nin section 1002(a) ( 21 U.S.C. 952(a) )\u2014\n**(A)**\nin the matter preceding paragraph (1), by inserting or drug or substance in schedule A after schedule I or II ; and\n**(B)**\nin paragraph (2), by inserting or drug or substances in schedule A after schedule I or II ;\n**(2)**\nin section 1003 ( 21 U.S.C. 953 )\u2014\n**(A)**\nin subsection (c), in the matter preceding paragraph (1), by inserting or drug or substance in schedule A after schedule I or II ; and\n**(B)**\nin subsection (d), by inserting or drug or substance in schedule A after schedule I or II ;\n**(3)**\nin section 1004(1) ( 21 U.S.C. 954(1) ), in the matter preceding subparagraph (A), by inserting or drug or substance in schedule A after schedule I ;\n**(4)**\nin section 1005 ( 21 U.S.C. 955 ), by inserting or drug or substance in schedule A after schedule I or II ; and\n**(5)**\nin section 1009(a) ( 21 U.S.C. 959(a) ), by inserting or drug or substance in schedule A after schedule I or II .\n#### 8. Sentencing review\n##### (a) Covered offense defined\nIn this section, the term covered offense means an offense involving a schedule A substance for which the penalty was established under section 4 or 5 of this Act.\n##### (b) Sentencing review\n**(1) Petition for review**\nIf a schedule A substance that is temporarily or permanently scheduled under section 201(k) of the Controlled Substances Act, as added by this Act, is subsequently descheduled or rescheduled on a schedule with lower penalties, any individual convicted of a covered offense involving such schedule A substance who is awaiting sentencing or is still serving a term of imprisonment for such covered offense on the date of the descheduling or rescheduling may petition the court that imposed the sentence for a sentencing reduction hearing for such covered offense.\n**(2) Sentencing review**\nNot later than 30 days after the date on which a petition is filed under paragraph (1), the court shall conduct a sentencing reduction hearing and may modify the sentence of the petitioner as if the descheduling or rescheduling described in paragraph (1) had been in effect on the date the covered offense was committed.\n#### 9. Rules of construction\nNothing in this Act, or the amendments made by this Act, may be construed to limit\u2014\n**(1)**\nthe prosecution of offenses involving controlled substance analogues under the Controlled Substances Act ( 21 U.S.C. 801 et seq. ); or\n**(2)**\nthe authority of the Attorney General to temporarily or permanently schedule, reschedule, or decontrol controlled substances under provisions of section 201 of the Controlled Substances Act ( 21 U.S.C. 811 ) that are in effect on the day before the date of enactment of this Act.",
      "versionDate": "2025-11-20",
      "versionType": "Introduced in Senate"
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-12-02T14:58:46Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3228is.xml"
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
      "title": "SIMSA Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-26T05:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SIMSA Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-26T05:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop the Importation and Manufacturing of Synthetic Analogues Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-26T05:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Controlled Substances Act to clarify how controlled substance analogues that are imported or offered for import are to be regulated, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-26T05:33:21Z"
    }
  ]
}
```
