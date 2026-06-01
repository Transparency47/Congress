# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6982?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6982
- Title: Preventing Prosecutors from Protecting Predators Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 6982
- Origin chamber: House
- Introduced date: 2026-01-08
- Update date: 2026-01-26T14:57:30Z
- Update date including text: 2026-01-26T14:57:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-08: Introduced in House
- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-01-08: Introduced in House

## Actions

- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-08",
    "latestAction": {
      "actionDate": "2026-01-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6982",
    "number": "6982",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Preventing Prosecutors from Protecting Predators Act of 2026",
    "type": "HR",
    "updateDate": "2026-01-26T14:57:30Z",
    "updateDateIncludingText": "2026-01-26T14:57:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-08",
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
      "actionDate": "2026-01-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-08",
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
          "date": "2026-01-08T15:00:30Z",
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
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6982ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 6982\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 8, 2026 Ms. Mace (for herself and Mr. Fine ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to provide for reporting requirements for certain grantees for grants to combat violence against women.\n#### 1. Short title\nThis Act may be cited as the Preventing Prosecutors from Protecting Predators Act of 2026 .\n#### 2. Grants to combat violence against women reporting requirements\n##### (a) In general\nPart T of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10441 et seq. ) is amended by adding at the end the following:\n2019. Prosecutorial data reporting (a) In general On an annual basis, each chief prosecuting officer of a covered office that serves a jurisdiction of 100,000 or more persons, if that jurisdiction receives funds under this part, shall submit to the Attorney General a report that contains, for the previous fiscal year, the following: (1) The total number of cases referred to the office for prosecution of a covered offense. (2) The number of cases involving a covered offense such office declined to prosecute and the reasoning for why the office declined to prosecute the covered offense. (3) The number of cases involving a covered offense initiated against a defendant\u2014 (A) previously arrested for an offense arising out of separate conduct; (B) previously convicted for an offense arising out of separate conduct; (C) with a pending case involving an offense arising out of separate conduct; (D) serving a term of probation for a conviction for an offense arising out of separate conduct; (E) currently on parole for a conviction for an offense arising out of separate conduct; and (F) currently or previously enrolled on the National Sex Offender Registry. (4) The number of defendants charged with a covered offense\u2014 (A) released on their own recognizance; (B) who were eligible for bail; (C) for whom the prosecutor requested bail and\u2014 (i) the type of bail requested; (ii) the amount of bail requested; and (iii) whether additional non-monetary conditions were requested; (D) for whom the court granted bail and\u2014 (i) the type of bail imposed; (ii) the amount of bail imposed; (iii) whether additional non-monetary conditions were requested or imposed; and (iv) outcomes after release on bail, including failure to appear or rearrest for an offense arising out of separate conduct; and (E) held in pretrial detention. (5) The number of defendants charged with a covered offense\u2014 (A) convicted of the covered offense as the result of a trial; (B) convicted of an offense as the result of a plea agreement; (C) found not guilty of the covered offense as the result of a trial; (D) whose cases ended in a mistrial; (E) whose charges were dismissed and the reasoning for each dismissal; and (F) whose charges were adjudicated by a diversion agreement, deferred prosecution agreement, or any substantively similar procedure and the reasoning for each agreement. (6) For cases involving a covered offense that resulted in a plea agreement reached with the defendant\u2014 (A) the number of such cases by each initial charge referred for prosecution; (B) the number of such cases by each charge that a defendant was convicted of as part of a plea-deal; (C) the number of such cases involving a defendant previously arrested for an offense arising out of separate conduct; (D) the number of such cases involving a defendant previously convicted for an offense arising out of separate conduct; (E) the number of such cases involving a defendant serving a term of probation for a conviction for an offense arising out of separate conduct; (F) the number of such cases involving a defendant released on parole for a conviction for an offense arising out of separate conduct; and (G) the number of such cases involving a defendant currently or previously enrolled on the National Sex Offender Registry. (7) For cases involving a covered offense that resulted in a conviction of the defendant at trial\u2014 (A) the number of such cases by each initial charge referred for prosecution; (B) the number of such cases involving a defendant previously arrested for an offense arising out of separate conduct; (C) the number of such cases involving a defendant previously convicted for an offense arising out of separate conduct; (D) the number of such cases involving a defendant serving a term of probation for a conviction for an offense arising out of separate conduct; (E) the number of such cases involving a defendant released on parole for a conviction for an offense arising out of separate conduct; (F) the number of such cases involving a defendant currently or previously enrolled on the National Sex Offender Registry; (G) the prosecutor\u2019s sentencing recommendation and justification; and (H) the actual sentence imposed. (b) Uniform standards The Attorney General shall define uniform standards for the reporting of the information required under this subsection, including the form such reports shall take and the process by which such reports shall be shared with the Attorney General. The Attorney General shall require each covered office to report information segregated by covered offense and organized in distinct sections reflecting prosecutions, bail conditions, plea agreements, and sentencing outcomes for each such offense. (c) Submission to judiciary committees The Attorney General shall submit the information received under this subsection to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives and shall publish such information on a publicly viewable website. (d) Covered offense defined In this subsection, the term covered offense means any of the following, and includes any attempt or conspiracy to commit any of the following: (1) Rape. (2) Sexual assault. (3) Domestic violence. (4) Domestic abuse or spousal abuse. (5) Production, possession, sale, or distribution of child sex abuse materials or child pornography. (6) Child abuse and neglect. (7) Sexual abuse or aggravated sexual abuse. (8) Child sexual abuse. (9) Forcible sodomy. (10) Murder or manslaughter committed before, during, or after a sex offense. (11) Incest. (12) Burglary with intent to commit a sex offense. (13) Voyeurism or video voyeurism. (14) Solicitation of a minor to engage in sexual conduct. (15) Solicitation of a minor to engage in or practice prostitution. (16) Endangering the welfare of a child. (17) Sexual exploitation of a minor. (18) Nonconsensual distribution of intimate images. (19) Sex trafficking. (e) Covered office defined In this section, the term covered office means any of the following: (1) The attorney general\u2019s office or substantively similar office of a State, Territory, or tribal jurisdiction. (2) The office of a subdivision of a State, territory, or Tribal jurisdiction responsible for prosecution, including a district attorney\u2019s office, state\u2019s attorney office, county attorney\u2019s office, city attorney\u2019s office or solicitor\u2019s office. (f) Penalties for noncompliance Beginning in the first fiscal year after the effective date of this section, the following shall apply: (1) If the chief executive of a covered office required to submit a report under this section fails to submit the required report, the Attorney General shall withhold not less than 25 percent and not more than 50 percent of funds otherwise allocable to that office under this part for the following fiscal year. (2) If the Attorney General determines that a covered office has declined to prosecute more than one-half of the total number of cases referred to it for prosecution of a covered offense during the preceding fiscal year, the Attorney General may\u2014 (A) require that office to submit a corrective action plan addressing prosecutorial practices and criteria for case declinations; (B) condition continued grants under this part on implementation of the corrective plan; and (C) in cases of repeated noncompliance or failure to implement such a plan, reduce or suspend future grant eligibility for that office for a period not to exceed two fiscal years. .",
      "versionDate": "2026-01-08",
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
        "updateDate": "2026-01-26T14:57:30Z"
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
      "date": "2026-01-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6982ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Omnibus Crime Control and Safe Streets Act of 1968 to provide for reporting requirements for certain grantees for grants to combat violence against women.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-23T03:59:02Z"
    },
    {
      "title": "Preventing Prosecutors from Protecting Predators Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-23T03:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preventing Prosecutors from Protecting Predators Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-23T03:53:16Z"
    }
  ]
}
```
