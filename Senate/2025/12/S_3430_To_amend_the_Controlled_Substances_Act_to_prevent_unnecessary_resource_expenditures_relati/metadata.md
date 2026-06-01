# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3430?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3430
- Title: PURE Act
- Congress: 119
- Bill type: S
- Bill number: 3430
- Origin chamber: Senate
- Introduced date: 2025-12-11
- Update date: 2026-01-08T19:40:11Z
- Update date including text: 2026-01-08T19:40:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in Senate
- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-12-11: Introduced in Senate

## Actions

- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3430",
    "number": "3430",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "PURE Act",
    "type": "S",
    "updateDate": "2026-01-08T19:40:11Z",
    "updateDateIncludingText": "2026-01-08T19:40:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-11",
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
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T15:08:48Z",
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
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "TX"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "TN"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3430is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3430\nIN THE SENATE OF THE UNITED STATES\nDecember 11, 2025 Mr. Kennedy (for himself, Mr. Cruz , Mr. Hagerty , and Mr. Graham ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Controlled Substances Act to prevent unnecessary resource expenditures relating to methamphetamine prosecutions.\n#### 1. Short title\nThis Act may be cited as the Preventing Unnecessary Resource Expenditures Act or the PURE Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nMethamphetamine is a powerful, highly addictive synthetic psychostimulant that affects the central nervous system. It can cause both short- and long-term adverse effects, including violent behavior, permanent neurological damage, and overdose death.\n**(2)**\nBeyond its destructive effects on individual health, methamphetamine abuse threatens communities, generates criminal behavior, produces unemployment, contributes to child neglect and abuse, and breaks up families.\n**(3)**\nDomestic production of illicit methamphetamine in the United States has decreased significantly. Over the past 20 years, clandestine methamphetamine laboratory seizures in the United States decreased from a high of 23,703 seizures in 2004 to 34 seizures in 2024.\n**(4)**\nHowever, according to the Centers for Disease Control and Prevention, between 2002 and 2023, the rate of overdose deaths involving psychostimulants, primarily methamphetamine, increased more than 35 times, with 0.3 deaths per 100,000 in 2002 and 10.6 deaths per 100,000 in 2023.\n**(5)**\nIn 2020, methamphetamine surpassed cocaine as the second most common drug involved in overdose deaths, after fentanyl, and it has remained in second place since then. According to the Centers for Disease Control and Prevention, from 2021 through 2023, methamphetamine was associated with 95,063 overdose deaths.\n**(6)**\nAccording to the 2024 National Drug Threat Assessment published by the Drug Enforcement Administration, 31 percent of drug-related deaths in the United States are caused by psychostimulants, mostly methamphetamine.\n**(7)**\nFrom 2021 through 2024, the Drug Enforcement Administration seized 182,000 kilograms of methamphetamine. By comparison, from 2001 through 2003, the Federal-wide Drug Seizure System showed a total seizure of 10,305 kilograms of methamphetamine.\n**(8)**\nThe sharp rise in methamphetamine offenses and overdoses can be attributed to Mexican cartels, which now produce the vast majority of the methamphetamine distributed in the United States.\n**(9)**\nThe People's Republic of China supplies the bulk of precursor chemicals that are used in the production of synthetic methamphetamine by Mexican drug cartels. In turn, Mexican cartels produce significant quantities of highly pure methamphetamine in large laboratories at low cost. The cartels then smuggle the illicit substance across the border into the United States.\n**(10)**\nMethamphetamine offenses now account for approximately half of all drug trafficking offenses sentenced federally.\n**(11)**\nUnder section 401 of the Controlled Substances Act ( 21 U.S.C. 841 ), the mandatory minimum sentences for manufacturing, distributing, or dispensing methamphetamine, or for possessing methamphetamine with the intent to manufacture, distribute, or dispense, are triggered based on the purity of the confiscated methamphetamine.\n**(12)**\nThe basis for the disparity in mandatory minimum thresholds between pure and impure methamphetamine was the fact that defendants in possession of pure methamphetamine were believed to be higher up in the distribution chain and thus more culpable.\n**(13)**\nAccording to the 2024 report on Methamphetamine Trafficking Offenses in the Federal Criminal Justice System by the United States Sentencing Commission, in 1988, when a majority of the methamphetamine distributed in the United States was produced by domestic laboratories, the average purity of methamphetamine was rarely greater than 50 percent. Today, it is rare for methamphetamine to test under 80 percent pure. According to the 2025 National Drug Threat Assessment published by the Drug Enforcement Administration, the methamphetamine tested in 2024 had an average purity of 95.1 percent.\n**(14)**\nThe shift towards purer methamphetamine occurred as Mexican cartels obtained greater market share of methamphetamine production and distribution beginning in the early 2000s. The average purity per kilogram of methamphetamine tested by the Drug Enforcement Administration in 2002 was 43 percent, but by 2005 the average purity was 80 percent.\n**(15)**\nThe requirement to establish purity in prosecutions of methamphetamine distribution places a significant burden on Federal and State crime laboratories, contributing to a waste of resources and the overburdening of laboratory technicians who are already backlogged.\n**(16)**\nThe purity requirement for methamphetamine prosecutions is no longer needed given the statistical improbability of any drug dealer distributing impure methamphetamine.\n**(17)**\nAt the same time, methamphetamine is a greater threat to the health, safety, and welfare of the people of the United States than it has ever been.\n#### 3. Adjustments to laboratory requirements in methamphetamine prosecutions\nPart D of the Controlled Substances Act ( 21 U.S.C. 841 et seq. ) is amended\u2014\n**(1)**\nin section 401(b)(1) ( 21 U.S.C. 841(b)(1) )\u2014\n**(A)**\nin subparagraph (A)(viii), by striking methamphetamine, its salts, isomers, and salts of its isomers or 500 grams or more of ; and\n**(B)**\nin subparagraph (B)(viii), by striking methamphetamine, its salts, isomers, and salts of its isomers or 50 grams or more of ;\n**(2)**\nin section 408 ( 21 U.S.C. 848 )\u2014\n**(A)**\nby redesignating subsection (s) as subsection (f); and\n**(B)**\nin subsection (f), as so redesignated, by inserting a mixture or substance containing a detectable amount of after involving ; and\n**(3)**\nin section 419a ( 21 U.S.C. 860a ), by inserting a mixture or substance containing a detectable amount of before methamphetamine .\n#### 4. Amendment to the sentencing guidelines\n##### (a) Directive\nPursuant to its authority under section 994 of title 28, United States Code, and in accordance with this section, the United States Sentencing Commission shall review and, as appropriate, amend the sentencing guidelines and policy statements applicable to persons convicted of offenses under section 401 of the Controlled Substances Act ( 21 U.S.C. 841 ) involving methamphetamine, its salts, isomers, and salts of its isomers, or related crimes involving the manufacture, distribution, or dispensing, or possessing with intent to manufacture, distribute, or dispense methamphetamine, its salts, isomers, and salts of its isomers.\n##### (b) Requirements\nIn carrying out this subsection, the Sentencing Commission shall\u2014\n**(1)**\ntake all appropriate measures to ensure that the sentencing guidelines and policy statements applicable to the offenses described in subsection (a) are sufficiently stringent to deter and adequately reflect the direct and aggregate harms caused to individuals, families, communities, and society by such offenses; and\n**(2)**\nconsider providing sentencing enhancements for those convicted of the offenses described in subsection (a) that\u2014\n**(A)**\ninvolve a large number of victims;\n**(B)**\ninvolve a pattern of continued and flagrant violations;\n**(C)**\ninvolve the use or threatened use of a dangerous weapon; or\n**(D)**\nresult in the death or bodily injury of any person.",
      "versionDate": "2025-12-11",
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
        "updateDate": "2026-01-08T19:40:11Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3430is.xml"
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
      "title": "PURE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T06:24:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PURE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Preventing Unnecessary Resource Expenditures Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Controlled Substances Act to prevent unnecessary resource expenditures relating to methamphetamine prosecutions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:18:33Z"
    }
  ]
}
```
