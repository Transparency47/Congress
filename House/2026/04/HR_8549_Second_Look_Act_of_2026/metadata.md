# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8549?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8549
- Title: Second Look Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8549
- Origin chamber: House
- Introduced date: 2026-04-28
- Update date: 2026-05-19T17:27:45Z
- Update date including text: 2026-05-19T17:27:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-28: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-28: Introduced in House

## Actions

- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-28",
    "latestAction": {
      "actionDate": "2026-04-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8549",
    "number": "8549",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "K000400",
        "district": "37",
        "firstName": "Sydney",
        "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
        "lastName": "Kamlager-Dove",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Second Look Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-19T17:27:45Z",
    "updateDateIncludingText": "2026-05-19T17:27:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-28",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-28",
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
          "date": "2026-04-28T13:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "NJ"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "NY"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "MI"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "GA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "IL"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "CA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "TN"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8549ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8549\nIN THE HOUSE OF REPRESENTATIVES\nApril 28, 2026 Ms. Kamlager-Dove (for herself, Mrs. McIver , Ms. Vel\u00e1zquez , Ms. Tlaib , Mr. Johnson of Georgia , Mr. Jackson of Illinois , Ms. Simon , Mr. Cohen , and Mr. Thanedar ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo enable incarcerated persons to petition a Federal court for a second look at sentences longer than 10 years, where the person is not a danger to the safety of any person or the community and has shown they are ready for reentry, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Second Look Act of 2026 .\n#### 2. Findings\n##### (a) Findings related to the united states criminal justice system\nCongress finds the following:\n**(1)**\nAlthough the United States has less than 5 percent of the world\u2019s population, the United States holds approximately 19 percent of the world\u2019s incarcerated population and has one of the highest rates of incarceration in the world, with more than 1,800,000 people incarcerated in State and Federal prisons and local jails.\n**(2)**\nThe jail and prison population of the United States has increased by more than 500 percent over a 40-year period preceding the date of enactment of this Act.\n**(3)**\nThe United States incarcerates citizens of the United States at 3 to 8 times the rate of other industrialized nations.\n**(4)**\nThe face of incarceration in the United States is not exclusively male. Although less than 5 percent of women in the world live in the United States, the United States houses nearly 30 percent of the world\u2019s incarcerated women and girls.\n**(5)**\nThe growth of the incarceration of women in the United States has outpaced that of men by nearly 2-to-1, growing more than 585 percent between 1980 and 2022. 58 percent of incarcerated women are mothers of minor children and most are the primary caretakers for their children.\n**(6)**\nThe overall prison population of the United States peaked in 2009 and declined at an average annual rate of 2.3 percent during the subsequent 12 years. At this pace, it would take until 2098, or 73 years, to return to the prison population of 1972, before the era of mass incarceration.\n**(7)**\nIn 2020, the prison population declined by 15 percent in response to safety precautions related to the COVID\u201319 pandemic, but most State prison populations, as well as the Federal prison population, have since bounced back up.\n**(8)**\nNearly 45 percent of the United States Federal prison population in 2024 is incarcerated for a drug trafficking offense.\n##### (b) Findings related to the need for a second look\nCongress finds the following:\n**(1)**\nA second look at the sentences for incarcerated individuals is needed.\n**(2)**\nLife sentences of imprisonment and long sentences without the possibility of review violate human rights standards.\n**(3)**\nOne out of 7 incarcerated individuals is currently serving a life sentence or a virtual life sentence of 50 years or longer. More than 25 percent of those individuals are sentenced to life without parole. One out of every 15 women in prison, or nearly 7,000 women, is serving a life sentence or virtual life sentence.\n**(4)**\nIn 2020, 147,920 people were serving a life sentence or virtual life sentence in the United States, and 55,945 people were serving a sentence of life without parole, compared to a total of 63 people serving a life sentence without the possibility of release in the United Kingdom.\n**(5)**\nMandatory minimum penalties continue to result in long sentences in the Federal prison system, and\u2014\n**(A)**\nas of 2016, 56 percent of the Federal prison population had been sentenced under a mandatory minimum provision;\n**(B)**\nduring fiscal years 2016 through 2021, nearly 25 percent of Federal prisoners sentenced to life or virtual life sentences were convicted of nonviolent crimes and 23 percent were convicted of drug trafficking offenses; and\n**(C)**\nin 2023, the average sentence length for individuals who were subject to a mandatory minimum penalty was 12.5 years of imprisonment.\n**(6)**\nAmong those individuals serving life sentences for drug-related convictions, 38 percent are in the Federal system.\n**(7)**\nThe United States has much more punitive sentencing laws than the rest of the world, as\u2014\n**(A)**\nsentence lengths in most European countries rarely exceed 20 years;\n**(B)**\nNorway abolished life sentences in 1981, and under Norwegian law, the maximum prison term is 21 years;\n**(C)**\nin Denmark and Sweden, individuals serving life sentences can be released after 12 years and 18 years of imprisonment, respectively; and\n**(D)**\nin Latin America, only 6 out of 19 countries maintain statutes that allow life imprisonment.\n**(8)**\nWith the abolition of parole under the Sentencing Reform Act of 1984 ( Public Law 98\u2013473 ; 98 Stat. 1987), there are extremely limited options for review of Federal sentences, which differs greatly from the rest of the world, as\u2014\n**(A)**\nBelgium requires a parole review of life sentences after 10 years;\n**(B)**\nGermany requires a parole review of life sentences after 15 years; and\n**(C)**\nthe International Criminal Court requires a parole review of life sentences after 25 years.\n**(9)**\nAn incarcerated individual should not be precluded from receiving a second look review of their sentence because of the nature of the crime for which the individual was convicted, as\u2014\n**(A)**\nindividuals tend to age out of criminal activity starting around 25 years of age;\n**(B)**\nreleased individuals over the age of 50 have a very low recidivism rate;\n**(C)**\nseveral studies, State policies and programs, and the National Institute of Corrections of the Bureau of Prisons consider incarcerated individuals aged 50 and above to be elderly;\n**(D)**\nincarcerated people age at an accelerated rate because they are more likely than the general public to experience stresses including long histories of alcohol and drug misuse, insufficient diet, lack of medical care, financial struggles, and stress of maintaining safety while behind bars;\n**(E)**\nthe Office of the Inspector General of the Department of Justice has found that aging inmates commit less misconduct while incarcerated and have a lower rate of re-arrest once released and has recommended the early release of aging inmates to help manage the inmate population and reduce costs at the Bureau of Prisons;\n**(F)**\nthe cost to State taxpayers to incarcerate the approximately 250,000 individuals aged 50 or older behind bars as of the date of enactment of this Act is approximately $16,000,000,000 each year;\n**(G)**\nincarceration of individuals beyond the age during which the individuals are likely to commit crime is a drain on taxpayer dollars that does nothing to increase public safety;\n**(H)**\nthe American Law Institute, the American Bar Association, the Task Force on Long Sentences of the Council on Criminal Justice, and the National Academy of Sciences recommend the enactment of resentencing opportunities for individuals serving long sentences;\n**(I)**\nindividuals are capable of redemption; and\n**(J)**\nin the words of Bryan Stevenson, each of us is more than the worst thing we've ever done .\n#### 3. Modification of certain terms of imprisonment\n##### (a) In general\nSubchapter C of chapter 229 of title 18, United States Code, is amended by inserting after section 3626 the following:\n3627. Modification of certain terms of imprisonment (a) In general Notwithstanding any other provision of law, a court may reduce a term of imprisonment imposed upon a defendant if\u2014 (1) the imposed term of imprisonment was more than 10 years; (2) the defendant has served not less than 10 years in custody for the offense; and (3) the court finds, after considering the factors set forth in subsection (c), that\u2014 (A) the defendant\u2014 (i) is not a danger to the safety of any person or the community; and (ii) demonstrates readiness for reentry; and (B) the interests of justice warrant a sentence modification. (b) Supervised release (1) In general Any defendant whose sentence is reduced pursuant to subsection (a), shall be ordered to serve\u2014 (A) the term of supervised release included as part of the original sentence imposed on the defendant; or (B) in the case of a defendant whose original sentence did not include a term of supervised release, a term of supervised release not to exceed the authorized terms of supervised release described in section 3583. (2) Conditions of supervised release The conditions of supervised release and any modification or revocation of the term of supervised release shall be in accordance with section 3583. (c) Factors and information To be considered in determining whether To modify a term of imprisonment (1) In general The court, in determining whether to reduce a term of imprisonment pursuant to subsection (a)\u2014 (A) may consider the factors described in section 3553(a), including the nature of the offense and the history and characteristics of the defendant; and (B) shall consider\u2014 (i) the age of the defendant at the time of the offense; (ii) the age of the defendant at the time of the sentence modification petition and relevant data regarding the decline in criminality as the age of a defendant increases; (iii) any presentation of argument and evidence by counsel for the defendant; (iv) a report and recommendation of the Bureau of Prisons, including information on whether the defendant has substantially complied with the rules of each institution in which the defendant has been confined and whether the defendant has completed any educational, vocational, or other prison program, where available; (v) any report and recommendation of the United States attorney for any district in which an offense for which the defendant is imprisoned was prosecuted; (vi) whether the defendant has demonstrated maturity, rehabilitation, and a fitness to reenter society sufficient to justify a sentence reduction; (vii) any statement, which may be presented orally or otherwise, by any victim of an offense for which the defendant is imprisoned or by a family member of the victim if the victim is deceased; (viii) any report from a physical, mental, or psychiatric examination of the defendant conducted by a licensed health care professional; (ix) the family and community circumstances of the defendant, including any history of abuse, trauma, or involvement in the child welfare system, and the potential benefits to children and family members of reunification with the defendant; (x) the role of the defendant in the offense and whether, and to what extent, an adult was involved in the offense if the defendant was a juvenile at the time of the offense; (xi) the diminished culpability of juveniles as compared to that of adults, and the hallmark features of youth, including immaturity, impetuosity, and failure to appreciate risks and consequences, if the defendant was a juvenile at the time of the offense; and (xii) any other information the court determines relevant to the decision of the court. (2) Rebuttable presumption In the case of a defendant who is 50 years of age or older on the date on which the defendant files an application for a sentence reduction under subsection (a), there shall be a rebuttable presumption that the defendant shall be released. (d) Limitation on applications pursuant to this section (1) Second application Not earlier than 5 years after the date on which an order denying release on an initial application under this section becomes final, a court shall entertain a second application by the same defendant under this section. (2) Third application Not earlier than 2 years after the date on which an order entered by a court on a second application under paragraph (1) becomes final, a court shall entertain a third application by the same defendant under this section. (3) Final application A court shall entertain a final application if the defendant\u2014 (A) is 50 years of age or older; and (B) has exhausted the sentencing modification process. (e) Procedures (1) Notice Not later than 30 days after the date on which the 10th year of imprisonment begins for a defendant sentenced to more than 10 years of imprisonment for an offense, the Bureau of Prisons shall provide written notice of this section to\u2014 (A) the defendant; and (B) the sentencing court, the United States attorney, and the Federal Public Defender or Executive Director of the Community Defender Organization for the judicial district in which the sentence described in this paragraph was imposed. (2) Application (A) In general An application for a sentence reduction under this section shall be filed in the judicial district in which the sentence was imposed as a motion to reduce the sentence of the defendant pursuant to this section and may include affidavits or other written material. (B) Requirement A motion to reduce a sentence under this section shall be filed with the sentencing court and a copy shall be served on the United States attorney for the judicial district in which the sentence was imposed. (3) Expanding the record; hearing (A) Expanding the record After the filing of a motion to reduce a sentence under this section, the court may direct the parties to expand the record by submitting additional written materials relating to the motion. (B) Hearing (i) In general The court shall, upon request of the defendant or the Government, conduct a hearing on the motion, at which the defendant and counsel for the defendant shall be given the opportunity to be heard. (ii) Evidence In a hearing under this section, the court shall allow parties to present evidence. (iii) Defendant\u2019s presence At a hearing under this section, the defendant shall be present unless the defendant waives the right to be present. The requirement under this clause may be satisfied by the defendant appearing by video teleconference. (iv) Counsel A defendant who is unable to afford counsel is entitled to have counsel appointed, at no cost to the defendant, to represent the defendant for the application and proceedings under this section, including any appeal, unless the defendant expressly waives the right to counsel after being fully advised of their rights by the court. (v) Findings The court shall state in open court, and file in writing, the reasons for granting or denying a motion under this section. (C) Appeal The Government or the defendant may file a notice of appeal in the district court for review of a final order under this section. The time limit for filing such appeal shall be governed by rule 4(a) of the Federal Rules of Appellate Procedure. (4) Crime victims rights Upon receiving an application under paragraph (2), the United States attorney shall provide any notifications required under section 3771. (f) Annual report (1) In general Not later than 1 year after the date of enactment of the Second Look Act of 2026 , and once every year thereafter, the United States Sentencing Commission shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report on requests for sentence reductions under this section. (2) Contents Each report required to be published under paragraph (1) shall include, for the 1-year period preceding the report\u2014 (A) the number of\u2014 (i) incarcerated individuals who were granted a sentence reduction under this section; and (ii) incarcerated individuals who were denied a sentence reduction under this section; (B) the number of incarcerated individuals released from prison under this section; (C) the demographic characteristics, including race and gender, of\u2014 (i) the incarcerated individuals who applied for a sentenced reduction under this section; (ii) the incarcerated individuals who were granted a sentence reduction under this section; and (iii) the incarcerated individuals who were released under this section; (D) the location, categorized by Federal circuit and State, of\u2014 (i) the incarcerated individuals who applied for a reduction under this section; (ii) the incarcerated individuals who were granted a reduction under this section; and (iii) the incarcerated individuals who were released under this section; (E) the average sentence reduction granted under this section; (F) the number of incarcerated individuals 50 years of age or older who applied for a sentence reduction under this section; (G) the number of incarcerated individuals who are 50 years of age or older who were granted a sentence reduction under this section; and (H) the number of incarcerated individuals 50 years of age or older who were released from prison under this section. (3) Attorney general cooperation The Attorney General shall\u2014 (A) assist and provide information to the United States Sentencing Commission in the performance of the duties of the Commission under this subsection; and (B) promptly respond to requests from the Commission. .\n##### (b) Table of sections\nThe table of sections for subchapter C of chapter 229 of title 18, United States Code, is amended by inserting after the item relating to section 3626 the following:\n3627. Modification of certain terms of imprisonment. .\n##### (c) Technical and conforming amendment\nSection 3582(c) of title 18, United States Code, is amended\u2014\n**(1)**\nin paragraph (1)(B), by striking and at the end;\n**(2)**\nin paragraph (2), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(3) the court may reduce a term of imprisonment in accordance with section 3627. .\n##### (d) Applicability\nThe amendments made by this section shall apply to any conviction entered before, on, or after the date of enactment of this Act.",
      "versionDate": "2026-04-28",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-05-19T17:27:44Z"
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
      "date": "2026-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8549ih.xml"
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
      "title": "Second Look Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-06T09:08:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Second Look Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-06T09:08:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To enable incarcerated persons to petition a Federal court for a second look at sentences longer than 10 years, where the person is not a danger to the safety of any person or the community and has shown they are ready for reentry, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-06T09:03:28Z"
    }
  ]
}
```
