# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1551?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1551
- Title: No Subsidies for Gender Transition Procedures Act
- Congress: 119
- Bill type: S
- Bill number: 1551
- Origin chamber: Senate
- Introduced date: 2025-05-01
- Update date: 2025-12-05T22:55:22Z
- Update date including text: 2025-12-05T22:55:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in Senate
- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-01: Introduced in Senate

## Actions

- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1551",
    "number": "1551",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "No Subsidies for Gender Transition Procedures Act",
    "type": "S",
    "updateDate": "2025-12-05T22:55:22Z",
    "updateDateIncludingText": "2025-12-05T22:55:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-01",
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
          "date": "2025-05-01T15:51:43Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "NE"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "LA"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1551is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1551\nIN THE SENATE OF THE UNITED STATES\nMay 1, 2025 Mr. Marshall (for himself, Mr. Ricketts , Mr. Cassidy , and Mr. Lee ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo deny tax deductions and other Federal funding for the costs of gender transition procedures.\n#### 1. Short title\nThis Act may be cited as the No Subsidies for Gender Transition Procedures Act .\n#### 2. Denial of medical expense tax deduction\n##### (a) In general\nSubsection (d) of section 213 of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(12) Expenses relating to gender transition (A) In general The term medical care does not include any gender transition procedure. (B) Definitions For purposes of this paragraph\u2014 (i) Gender transition procedure (I) In general The term gender transition procedure means any hormonal or surgical intervention for the purpose of gender transition, including\u2014 (aa) the provision of gonadotropin-releasing hormone agonists or other puberty-suppression drugs or puberty-blocking drugs to stop or delay normally-timed puberty in an individual who does not identify as his or her sex, (bb) the provision of testosterone, estrogen, progesterone, or other androgen blockers to an individual at doses which are supraphysiologic to what would normally be produced endogenously in a healthy individual of the same age and sex, with the intent to align an individual's physical appearance with an identity that differs from his or her sex, (cc) surgical procedures that attempt to transform an individual's physical appearance to align with an identity that differs from his or her sex or that attempt to alter or remove an individual's sexual organs to minimize or destroy their natural biological functions, (dd) castration, vasectomy, penectomy, orchiectomy, vaginoplasty, clitoroplasty, vulvoplasty, mastectomy, hysterectomy, oophorectomy, ovariectomy, reconstruction of the fixed part of the urethra with or without metoidioplasty or phalloplasty, metoidioplasty, phalloplasty, vaginectomy, scrotoplasty, implantation of erection or testicular prostheses, reduction thyrochondroplasty, chondrolaryngoplasty, tubal ligation, sterilization, augmentation mammoplasty, placement of chest implants to create feminine breasts, placement of fat or artificial implants in the gluteal region, liposuction, lipofilling, voice surgery, hair reconstruction, pectoral implants, any plastic, cosmetic, or aesthetic surgery which feminizes or masculinizes the facial or other physiological features of an individual, and any removal of any otherwise healthy or non-diseased body part or tissue. (II) Exclusions The term gender transition procedure does not include, when furnished to an individual by a health care provider with the consent of such individual (or, if applicable, such individual\u2019s parents or legal guardian)\u2014 (aa) services to individuals born with a medically verifiable disorder of sex development, including an individual with external sex characteristics which are irresolvably ambiguous, such as an individual born with 46 XX chromosomes with virilization, an individual born with 46 XY chromosomes with undervirilization, or an individual born having both ovarian and testicular tissue, (bb) services relating to any other physician-diagnosed disorder of sexual development with respect to which the physician has determined through genetic or biochemical testing that the individual does not have normal sex chromosome structure, sex steroid hormone production, or sex steroid hormone action for a healthy male or female of the same age, (cc) the treatment of any infection, injury, disease, or disorder caused or exacerbated by the performance of gender transition procedures, without regard to whether the gender transition procedure was performed in accordance with State and Federal law or whether the gender transition procedure is treated as medical care under this section, (dd) any procedure undertaken because the individual suffers from a physical disorder, physical injury, or physical illness (but not mental, behavioral, or emotional distress or a mental, behavioral, or emotional disorder) which would, as certified by a physician, place the individual in imminent danger of death or impairment of major bodily function unless the procedure is performed to alleviate said physical disorder, physical injury, or physical illness, (ee) procedures to restore or reconstruct the body of the individual in order to correspond to the individual's sex after one or more previous gender transition procedures, which may include the removal of a pseudo phallus or breast augmentation, (ff) puberty suppression or puberty-blocking prescription drugs for the purpose of normalizing puberty for a minor experiencing precocious puberty, or (gg) male circumcision. (ii) Gender transition The term gender transition means the process by which an individual goes from identifying with or presenting as his or her sex to identifying with or presenting as a self-proclaimed identity which does not correspond with or is different from his or her sex, and may be accompanied by social, legal, or physical changes. (iii) Sex The term sex , when referring to an individual\u2019s sex, means either male or female, as biologically determined. (iv) Female The term female , when used to refer to a natural person, means a person belonging, at conception, to the sex characterized by a reproductive system with the biological function of producing eggs (ova). (v) Male The term male , when used to refer to a natural person, means a person belonging, at conception, to the biological sex characterized by a reproductive system with the biological function of producing sperm. .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 3. Prohibiting Federal medicaid funding for gender transition procedures\n##### (a) In general\nSection 1903(i) of the Social Security Act ( 42 U.S.C. 1396b(i) ) is amended\u2014\n**(1)**\nin paragraph (26), by striking ; or and inserting a semicolon;\n**(2)**\nin paragraph (27), by striking the period at the end and inserting ; or ;\n**(3)**\nby inserting after paragraph (27) the following new paragraph:\n(28) with respect to any amounts expended for any specified gender transition procedure (as defined in section 1905(kk)) to an individual enrolled in a State plan under this title (or a waiver of such plan), including any amounts expended for the administration of a State program that furnishes any such procedure. ; and\n**(4)**\nin the flush left matter at the end, by striking and (18), and inserting (18), and (28) .\n##### (b) Prohibiting Federal medicaid funding for gender transition procedures\nSection 1905 of the Social Security Act ( 42 U.S.C. 1396d ) is amended by adding at the end the following new subsection:\n(kk) Prohibiting Federal medicaid funding for specified gender transition procedures (1) Specified gender transition procedures defined For purposes of section 1903(i)(28), except as provided in paragraph (2), the term specified gender transition procedure means, with respect to an individual, any hormonal or surgical intervention for the purpose of gender transition, including\u2014 (A) the provision of gonadotropin-releasing hormone agonists or other puberty suppression drugs or puberty-blocking drugs to stop or delay normally timed puberty in an individual who does not identify as his or her sex; (B) the provision of testosterone, estrogen, progesterone, or other androgen blockers to an individual at doses which are supraphysiologic to what would normally be produced endogenously in a healthy individual of the same age and sex, with the intent to align an individual\u2019s physical appearance with an identity that differs from his or her sex; (C) surgical procedures that attempt to transform an individual\u2019s physical appearance to align with an identity that differs from his or her sex or that attempt to alter or remove an individual\u2019s sexual organs to minimize or destroy their natural biological functions; or (D) castration, vasectomy, penectomy, orchiectomy, vaginoplasty, clitoroplasty, vulvoplasty, mastectomy, hysterectomy, oophorectomy, ovariectomy, reconstruction of the fixed part of the urethra with or without metoidioplasty or phalloplasty, metoidioplasty, phalloplasty, vaginectomy, scrotoplasty, implantation of erection or testicular prostheses, reduction thyrochondroplasty, chondrolaryngoplasty, tubal ligation, sterilization, augmentation mammoplasty, placement of chest implants to create feminine breasts, placement of fat or artificial implants in the gluteal region, liposuction, lipofilling, voice surgery, hair reconstruction, pectoral implants, any plastic, cosmetic, or aesthetic surgery which feminizes or masculinizes the facial or other physiological features of an individual, and any removal of any otherwise healthy or non-diseased body part or tissue. (2) Exclusions The term specified gender transition procedure shall not include, when furnished to an individual by a health care provider with the consent of such individual (or, if applicable, the parents or legal guardian of such individual)\u2014 (A) services to individuals born with a medically verifiable disorder of sex development, including an individual with external sex characteristics which are irresolvably ambiguous, such as an individual born with 46 XX chromosomes with virilization, an individual born with 46 XY chromosomes with undervirilization, or an individual born having both ovarian and testicular tissue; (B) services relating to any other physician-diagnosed disorder of sexual development with respect to which the physician has determined through genetic or biochemical testing that the individual does not have normal sex chromosome structure, sex steroid hormone production, or sex steroid hormone action for a healthy male or female of the same age; (C) the treatment of any infection, injury, disease, or disorder caused or exacerbated by the performance of gender transition procedures, without regard to whether the gender transition procedure was performed in accordance with State and Federal law or whether the gender transition procedure is treated as medical care under this section; (D) any procedure undertaken because the individual suffers from a physical disorder, physical injury, or physical illness (but not mental, behavioral, or emotional distress or a mental, behavioral, or emotional disorder) which would, as certified by a physician, place the individual in imminent danger of death or impairment of major bodily function unless the procedure is performed to alleviate said physical disorder, physical injury, or physical illness; (E) any procedure to restore or reconstruct the body of the individual in order to correspond to the individual\u2019s sex after 1 or more previous gender transition procedures, which may include the removal of a pseudo phallus or breast augmentation; (F) puberty suppression or puberty-blocking prescription drugs for the purpose of normalizing puberty for an individual experiencing precocious puberty; or (G) male circumcision. (3) Additional definitions For purposes of this subsection: (A) Gender transition The term gender transition means the process by which an individual goes from identifying with or presenting as his or her sex to identifying with or presenting as a self-proclaimed identity which does not correspond with or is different from his or her sex, and may be accompanied by social, legal, or physical changes. (B) Sex The term sex , when referring to an individual\u2019s sex, means either male or female, as biologically determined, including as described in subparagraphs (C) and (D). (C) Female The term female , when used to refer to a natural person, means an individual belonging, at conception, to the sex characterized by a reproductive system with the biological function of producing eggs (ova). (D) Male The term male , when used to refer to a natural person, means an individual belonging, at conception, to the biological sex characterized by a reproductive system with the biological function of producing sperm. .\n##### (c) Effective date\nThe amendments made by this section shall apply to services furnished on or after the date of the enactment of this Act.\n#### 4. Prohibiting Federal children\u2019s health insurance program funding for gender transition procedures on minors\n##### (a) In general\nSection 2105(c) of the Social Security Act ( 42 U.S.C. 1397ee(c) ) is amended by adding at the end the following new paragraph:\n(13) Limitation on payment for specified gender transition procedures for minors Payment shall not be made to a State under this section for any amount expended under the State plan to pay for specified gender transition procedures (as defined in section 1905(kk)) or to assist in the purchase, in whole or in part, of health benefit coverage that includes coverage of any such procedure. .\n##### (b) Conforming amendment\nSection 2107(e)(1)(N) of the Social Security Act ( 42 U.S.C. 1397gg(e)(1)(N) ) is amended by striking and (17) and inserting (17), and (28) .\n##### (c) Effective date\nThe amendments made by this section shall apply to services furnished on or after the date of the enactment of this Act.\n#### 5. Prohibiting Federal medicare funding for gender transition procedures\n##### (a) In general\nSection 1862(a) of the Social Security Act ( 42 U.S.C. 1395y(a) ) is amended\u2014\n**(1)**\nin paragraph (24), by striking or at the end;\n**(2)**\nin paragraph (25), by striking the period at the end and inserting ; or ; and\n**(3)**\nby inserting after paragraph (25) the following new paragraph:\n(26) which are specified gender transition procedures (as defined in section 1905(kk)). .\n##### (b) Effective date\nThe amendments made by subsection (a) shall apply to items and services furnished on or after the date of the enactment of this Act.\n#### 6. Exclusion of gender transition procedures from essential health benefits\nSection 1302(b)(2) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18022(b)(2) ) is amended\u2014\n**(1)**\nin the paragraph heading, by striking Limitation and inserting Limitations ;\n**(2)**\nby redesignating subparagraph (B) as subparagraph (C);\n**(3)**\nby inserting after subparagraph (A) the following:\n(B) Exclusions In defining the essential health benefits under paragraph (1), or in revising essential health benefits under paragraph (4)(H), the Secretary shall not include the category of gender transition procedures (as defined in section 213(d)(12)(B) of the Internal Revenue Code of 1986) or any items or services covered within such a category. ; and\n**(4)**\nin subparagraph (C) (as so redesignated), by striking paragraph (2) and inserting subparagraph (A) .",
      "versionDate": "2025-05-01",
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
        "actionDate": "2025-05-05",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3205",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "No Subsidies for Gender Transition Procedures Act",
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
        "name": "Health",
        "updateDate": "2025-05-21T14:02:01Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1551is.xml"
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
      "title": "No Subsidies for Gender Transition Procedures Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-14T04:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Subsidies for Gender Transition Procedures Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-14T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to deny tax deductions and other Federal funding for the costs of gender transition procedures.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-14T04:18:45Z"
    }
  ]
}
```
