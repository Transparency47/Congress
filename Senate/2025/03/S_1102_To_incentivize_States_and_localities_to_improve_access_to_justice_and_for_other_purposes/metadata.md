# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1102?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1102
- Title: Quality Defense Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1102
- Origin chamber: Senate
- Introduced date: 2025-03-25
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in Senate
- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-03-25: Introduced in Senate

## Actions

- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1102",
    "number": "1102",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Quality Defense Act of 2025",
    "type": "S",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
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
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T15:09:56Z",
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
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "IL"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1102is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1102\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2025 Mr. Booker (for himself, Mr. Durbin , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo incentivize States and localities to improve access to justice, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Providing a Quality Defense Act of 2025 or the Quality Defense Act of 2025 .\n#### 2. Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto protect the constitutional rights to due process and a fair criminal prosecution under the Fifth, Sixth, and Fourteenth Amendments to the Constitution of the United States, including the right to counsel, in State and local courts, as articulated by the Supreme Court of the United States in Gideon v. Wainwright, 372 U.S. 335 (1963), and its progeny;\n**(2)**\nto protect the right to counsel for juveniles in delinquency proceedings, including the determination of whether a juvenile should be tried as an adult, under the Due Process Clause of the Fourteenth Amendment as articulated by the Supreme Court in In re Gault, 387 U.S. 1 (1967);\n**(3)**\nto collect data related to public defense in order to facilitate evidence-based reforms and improvements; and\n**(4)**\nto ensure that compensation for public defenders and panel attorneys reflects the constitutional guarantee of the right to counsel and does not disincentivize attorneys from pursuing a career in public defense.\n#### 3. Definitions\nIn this Act, except as otherwise provided in section 7:\n**(1) Applicable public defender's office**\nThe term applicable public defender's office , with respect to an eligible entity that is\u2014\n**(A)**\na public defender's office, means the eligible entity;\n**(B)**\na State or unit of local government, means\u2014\n**(i)**\nthe public defender's office of the eligible entity; and\n**(ii)**\na public defender's office of a unit of local government within the eligible entity; and\n**(C)**\na Tribal organization, means the public defender's office of the Tribal organization.\n**(2) Assigned counsel program**\nThe term assigned counsel program means a program or procedure by which a court assigns a panel attorney to provide quality legal representation to a client.\n**(3) Case**\nThe term case includes all charges against an individual involved in a single incident of alleged criminal or delinquent conduct.\n**(4) Case type**\n**(A) In general**\nThe term case type means the classification of a client\u2019s case into 1 of the following categories, as defined under State or local law:\n**(i)**\nJuvenile.\n**(ii)**\nMisdemeanor.\n**(iii)**\nFelony for which the death penalty may be imposed.\n**(iv)**\nFelony for which a sentence of up to life imprisonment may be imposed.\n**(v)**\nFelony not described in clause (iii) or (iv).\n**(vi)**\nViolation of probation or parole.\n**(vii)**\nSchool proceeding.\n**(viii)**\nOther.\n**(B) Multiple charges**\nIf a case involves multiple charges, the case type shall be determined according to the most serious charge under the applicable State or local law.\n**(5) Corresponding prosecutor's office**\nThe term corresponding prosecutor's office , with respect to a public defender\u2019s office or panel attorneys, means a prosecutorial unit that appears adverse to the public defender\u2019s office or panel attorneys in criminal proceedings.\n**(6) Data grant**\nThe term data grant means a grant awarded under section 4(a)(1).\n**(7) Eligible entity**\nThe term eligible entity means a State, unit of local government, Tribal organization, public defender's office, or assigned counsel program that\u2014\n**(A)**\nin the case of an application for a data grant, has not, as of the date of application, developed and implemented a data collection process that meets the requirements under section 4(b)(2); and\n**(B)**\nin the case of an application for a hiring grant, as of the date of the application, has\u2014\n**(i)**\nreceived a data grant; and\n**(ii)**\nfulfilled the requirements of the data grant.\n**(8) Hiring grant**\nThe term hiring grant means a grant awarded under section 4(a)(2).\n**(9) Most serious charge**\nThe term most serious charge , with respect to a case that involves multiple charges, means the charge that carries the most severe or lengthy maximum penalty.\n**(10) Panel attorney**\nThe term panel attorney means a private attorney assigned by the court who serves the same function as a public defender, without regard to whether the role is full-time or part-time.\n**(11) Prosecutor**\nThe term prosecutor \u2014\n**(A)**\nhas the meaning given the term in section 3001(b) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10671(b) ); and\n**(B)**\nincludes a full-time employee of a Tribal organization who\u2014\n**(i)**\nis continually licensed to practice law; and\n**(ii)**\ncarries out activities equivalent to those of a prosecutor referred to in subparagraph (A).\n**(12) Public defender**\nThe term public defender \u2014\n**(A)**\nhas the meaning given the term in section 3001(b) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10671(b) ); and\n**(B)**\nincludes an attorney employed by a Tribal organization who\u2014\n**(i)**\nis continually licensed to practice law; and\n**(ii)**\ncarries out activities equivalent to those of a public defender referred to in subparagraph (A).\n**(13) Prosecutor's office; public defender's office**\nThe terms prosecutor's office and public defender's office mean an agency or office of a State, unit of local government, or Tribal organization that employs prosecutors or public defenders, respectively.\n**(14) Resolution**\nThe term resolution , with respect to a case, means the manner in which the case concludes, including by\u2014\n**(A)**\ndismissal by the prosecutor;\n**(B)**\ndismissal based on a motion, such as a motion to suppress evidence;\n**(C)**\na plea agreement at first appearance;\n**(D)**\na plea agreement entered into at any point in the criminal prosecution other than first appearance;\n**(E)**\ndiversion; or\n**(F)**\na bench or jury trial and the outcome of the trial, including the sentence if the defendant is convicted of any offense charged.\n**(15) Secondary charge**\nThe term secondary charge , with respect to a case that involves multiple charges, means any charge that is not the most serious charge.\n**(16) State**\nThe term State has the meaning given the term in section 901 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10251 ).\n**(17) Tribal organization**\nThe term Tribal organization has the meaning given the term tribal organization in section 4(l) of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304(l) ).\n**(18) Unit of local government**\nThe term unit of local government has the meaning given the term in section 901 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10251 ).\n#### 4. Public defense grant program\n##### (a) Grant authority\nThe Attorney General may award a grant to an eligible entity to\u2014\n**(1)**\ndevelop, implement, and update a data collection process under subsection (b)(2); or\n**(2)**\nhire additional public defense attorneys or carry out related activities under subsection (c)(3).\n##### (b) Data grants\n**(1) Term**\nThe term of a data grant shall be 3 fiscal years.\n**(2) Required data collection**\nAn eligible entity that receives a data grant shall develop and implement a process for collecting the following data for attorneys employed by each applicable public defender\u2019s office, and for panel attorneys within the jurisdiction of the eligible entity, during each fiscal year of the grant period:\n**(A)**\nThe mean number of hours per month worked per attorney.\n**(B)**\nThe mean number of hours spent per month by an attorney on\u2014\n**(i)**\ndiscovery and investigation, including witness interviews;\n**(ii)**\ncourt time, including preparation and appearances;\n**(iii)**\nclient communication and care;\n**(iv)**\nresearch and writing, including motions practice; and\n**(v)**\nadministrative work.\n**(C)**\nThe number of cases handled, broken down by\u2014\n**(i)**\ncase type, including by\u2014\n**(I)**\nthe most serious charge; and\n**(II)**\neach secondary charge;\n**(ii)**\nthe race, ethnicity, age, and gender of the client;\n**(iii)**\nthe date on which the attorney was appointed to the case;\n**(iv)**\nwhether the case remained open as of the last day of the fiscal year, and if not, the date on which the case was closed; and\n**(v)**\nthe resolution of the case, if the case was concluded by the last day of the fiscal year.\n**(D)**\nAny other information as the Attorney General determines appropriate.\n**(3) Renewal**\nUpon application from an eligible entity that received a data grant, the Attorney General may award a subsequent data grant to the eligible entity for an additional term that may begin upon termination of the initial data grant.\n##### (c) Hiring grants\n**(1) Application requirements**\nAn eligible entity desiring a hiring grant shall submit to the Attorney General an application that includes, as of the date of the application\u2014\n**(A)**\nthe caseload and number of, and pay scale for, attorneys and other staff of each applicable public defender's office; and\n**(B)**\n**(i)**\nthe number of panel attorneys within the jurisdiction of the eligible entity;\n**(ii)**\nthe total number of cases assigned to the attorneys described in clause (i); and\n**(iii)**\nthe average number of hours spent on a case by an attorney described in clause (i).\n**(2) Term**\nThe term of a hiring grant shall be 3 years.\n**(3) Use of funds**\nAn eligible entity may use a hiring grant to\u2014\n**(A)**\nhire additional public defenders;\n**(B)**\nincrease compensation for public defenders or panel attorneys to achieve pay parity with corresponding prosecutor's offices;\n**(C)**\nhire case workers, social workers, investigators, or paralegals; or\n**(D)**\nestablish or fund a loan assistance program for public defenders.\n**(4) Supplement, not supplant**\nAn eligible entity may not use a hiring grant to supplant funds that the eligible entity would otherwise have used for any authorized purpose described in paragraph (3) during the grant period.\n**(5) Required data collection**\nDuring each fiscal year of the grant period, an eligible entity that receives a hiring grant shall collect the data described in subsection (b)(2).\n##### (d) Submission requirement\nNot later than 60 days after the end of a fiscal year, an eligible entity that receives a data grant or hiring grant shall submit to the Attorney General the data described in subsection (b)(2) for that fiscal year.\n##### (e) Multiple defendants\nIf a prosecutor\u2019s charging document states that multiple defendants were involved in a single incident of alleged criminal or delinquent conduct, each defendant shall be considered a separate case for purposes of the collection of data described in subsection (b)(2).\n##### (f) Authorization of appropriations\nThere are authorized to be appropriated to the Attorney General to carry out this section\u2014\n**(1)**\n$250,000,000 for each of the first 5 fiscal years beginning after the date of enactment of this Act; and\n**(2)**\nsuch sums as may be necessary for each fiscal year thereafter.\n#### 5. Studies\n##### (a) Studies\n**(1) Caseload limits study**\n**(A) In general**\nAfter the end of the first fiscal year for which data grants are awarded, the Attorney General, acting through the Director of the Bureau of Justice Assistance and the Director of the Office for Access to Justice, shall\u2014\n**(i)**\nconduct a study to analyze the data submitted to the Attorney General under section 4(d) for that fiscal year related to public defender and panel attorney caseloads and correlated outcomes;\n**(ii)**\nreview studies, reports, and other data published or provided by professional organizations, legal associations, and bar associations related to public defender and panel attorney caseloads; and\n**(iii)**\ndevelop and publish best practices and recommendations for setting public defender and panel attorney caseloads based on the information described in clauses (i) and (ii) to ensure\u2014\n**(I)**\nreasonably effective assistance of counsel pursuant to constitutional standards and prevailing professional norms; and\n**(II)**\ncompetent representation pursuant to applicable rules of professional responsibility.\n**(B) Continuing study**\nNot less frequently than once every 5 years, the Attorney General shall\u2014\n**(i)**\nstudy and review new studies, reports, or other data as described in subparagraph (A)(ii); and\n**(ii)**\nupdate the best practices and recommendations under subparagraph (A)(iii).\n**(2) Compensation study**\nNot later than 3 years after the date of enactment of this Act, the Attorney General, acting through the Director of the Bureau of Justice Assistance and the Director of the Office for Access to Justice, shall\u2014\n**(A)**\nconduct a national study of public defender salaries and panel attorney rates, using prosecutors\u2019 salaries as one benchmark; and\n**(B)**\ndevelop and publish best practices and recommendations relating to compensation of public defenders and panel attorneys.\n##### (b) Authorization of appropriations\nThere are authorized to be appropriated to the Attorney General such sums as may be necessary to carry out this section.\n#### 6. State data collection\n##### (a) In general\nFor any fiscal year beginning after the date of enactment of this Act, a State that receives funds under subpart 1 of part E of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10151 et seq. ) may submit to the Office for Access to Justice of the Department of Justice data on, with respect to criminal cases heard by a court of the State or of a unit of local government in the State during that fiscal year, the number of cases for which a defendant was represented in court by a public defender or panel attorney, broken down by\u2014\n**(1)**\nthe most serious charge and the total number of secondary charges in each case; and\n**(2)**\nrace, ethnicity, age, and gender of the defendant.\n##### (b) Applicable criminal offenses\nA State that elects to submit data under subsection (a) shall include data with respect to\u2014\n**(1)**\ncriminal offenses for which a term of imprisonment of more than 1 year may be imposed;\n**(2)**\ncriminal offenses for which a term of imprisonment of 1 year or less may be imposed, including misdemeanors, traffic violations, and violations of municipal ordinances; and\n**(3)**\nacts of juvenile delinquency or juvenile status offenses for which any term of detention may be imposed.\n##### (c) Funding\nA State that receives funds under subpart 1 of part E of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10151 et seq. ) may apply for, and the Attorney General may award, a 5 percent increase in those funds, to be used by the State to collect and provide to the Office for Access to Justice of the Department of Justice the data described in subsection (a) of this section.\n#### 7. Funding for educational programs\n##### (a) Definition\nIn this section, the term eligible entity means an entity that is\u2014\n**(1)**\nan organization\u2014\n**(A)**\ndescribed in paragraph (3) or (6) of section 501(c) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of such Code; or\n**(B)**\nfunded by a State or unit of local government; or\n**(2)**\na State, unit of local government, Indian Tribal government, or political subdivision of an Indian Tribe.\n##### (b) Grants\nThe Attorney General shall award grants to eligible entities to provide a comprehensive educational program to public defenders and panel attorneys that offers\u2014\n**(1)**\nongoing training and support; and\n**(2)**\nprogramming that includes\u2014\n**(A)**\nskills training, including pretrial practice, negotiation skills, trial skills, and sentencing advocacy;\n**(B)**\nclient-centered values;\n**(C)**\nimplicit bias training;\n**(D)**\nleadership development; and\n**(E)**\nongoing support to reinforce the training curriculum.\n##### (c) Authorization of appropriations\nThere are authorized to be appropriated to the Attorney General to carry out this section $5,000,000 for each of the first 5 fiscal years beginning after the date of enactment of this Act.",
      "versionDate": "2025-03-25",
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
        "updateDate": "2025-04-06T11:29:14Z"
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
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1102is.xml"
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
      "title": "Quality Defense Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-05T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Quality Defense Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-05T04:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Providing a Quality Defense Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-05T04:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to incentivize States and localities to improve access to justice, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-05T04:18:20Z"
    }
  ]
}
```
