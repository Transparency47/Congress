# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2469?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2469
- Title: College Athlete Right to Organize Act
- Congress: 119
- Bill type: S
- Bill number: 2469
- Origin chamber: Senate
- Introduced date: 2025-07-28
- Update date: 2025-12-05T21:30:24Z
- Update date including text: 2025-12-05T21:30:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-28: Introduced in Senate
- 2025-07-28 - IntroReferral: Introduced in Senate
- 2025-07-28 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-07-28: Introduced in Senate

## Actions

- 2025-07-28 - IntroReferral: Introduced in Senate
- 2025-07-28 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-28",
    "latestAction": {
      "actionDate": "2025-07-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2469",
    "number": "2469",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "M001169",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Murphy, Christopher [D-CT]",
        "lastName": "Murphy",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "College Athlete Right to Organize Act",
    "type": "S",
    "updateDate": "2025-12-05T21:30:24Z",
    "updateDateIncludingText": "2025-12-05T21:30:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-28",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-28",
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
          "date": "2025-07-28T19:53:55Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "MA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-07-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2469is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2469\nIN THE SENATE OF THE UNITED STATES\nJuly 28, 2025 Mr. Murphy (for himself, Ms. Warren , and Mr. Sanders ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo establish collective bargaining rights for college athletes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the College Athlete Right to Organize Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe National Labor Relations Act ( 29 U.S.C. 151 et seq. ) seeks to remedy the inequality of bargaining power between employees and employers primarily through establishing and protecting the rights of employees to self-organize and designate representatives of their own choosing for the purpose of negotiating the terms and conditions of their employment or other mutual aid or protection.\n**(2)**\nLabor organizations often originate to remedy unfair and exploitative labor practices by employers through assisting employees in securing more equitable terms and conditions of their employment, including fair compensation and safe working conditions, which individual employees would be unlikely to negotiate successfully for on their own.\n**(3)**\nLabor organizations serve unique and essential purposes for professional athletes competing in sports leagues, where it is desirable to establish uniform rules and standards across multiple employers. These rules and standards bear significant consequences to the athletes in terms of compensation, health and safety, and the ability or lack thereof for athletes to choose their employer, among other issues related to the athletes\u2019 well-being.\n**(4)**\nThe formation of labor organizations representing athletes in professional sports leagues in the United States has helped end exploitative practices by team owners and management, particularly through establishing collective-bargaining agreements that have secured athletes a fair share of the revenues their talent and labor produces, as well as more equitable terms of their employment and protections for their short- and long-term health.\n**(5)**\nCollege athletes face exploitative and unfair labor practices by the National Collegiate Athletic Association (referred to in this section as the NCAA ) and its member institutions, primarily through the denial of the basic economic and labor rights of such athletes, which the NCAA and its member institutions have justified by defining college athletes as amateurs.\n**(6)**\nThe NCAA and its member institutions have denied college athletes a fair wage for their labor by colluding to cap compensation; they maintain strict and exacting control over the terms and conditions of college athletes\u2019 labor; and they exercise the ability to terminate an athlete\u2019s eligibility to compete if the athlete violates these terms and conditions.\n**(7)**\nCollege athletes exhibit the markers of employment as established under the common law definition of the term employee : They perform a valuable service for their respective colleges under a contract for hire in the form of grant-in-aid agreements; these agreements assert significant control over how athletes perform their work and the conditions under which they work; and they receive compensation in the form of grant-in-aid and stipends in exchange for their athletic services.\n**(8)**\nTo establish more equitable terms and conditions for college athletes\u2019 labor, college athletes need representation of their own choosing to negotiate collective-bargaining agreements with their respective colleges and the athletic conferences that help set rules and standards across an entire league.\n**(9)**\nTo organize effectively, college athletes must be able to form collective bargaining units across institutions of higher education that compete against each other, including within athletic conferences; and, accordingly, to establish effective collective bargaining rights for college athletes under this Act, the National Labor Relations Act must be amended to cover both private and public institutions of higher education to the extent that college athletes attending such institutions fall within the definition of employee under that Act, as amended by this Act.\n**(10)**\nThe Constitution of the United States vests Congress with the power to regulate commerce between the States, and intercollegiate sports, which are maintained by athletic associations that host competitions between colleges across States, involves interstate commerce that generates annual revenue of more than $15,000,000,000.\n**(11)**\nIntercollegiate sports\u2019 significant engagement in interstate commerce justifies application of the National Labor Relations Act ( 29 U.S.C. 151 et seq. ) to regulate the labor market within which public and private institutions of higher education compete and set rules pertaining to the wages and working conditions of college athletes.\n#### 3. Collective bargaining rights of college athletes\n##### (a) Definitions\nSection 2 of the National Labor Relations Act ( 29 U.S.C. 152 ) is amended\u2014\n**(1)**\nin paragraph (2), by adding at the end the following: Notwithstanding the previous sentence, the term employer includes a public institution of higher education with respect to the employment of college athlete employees of the institution. ;\n**(2)**\nin paragraph (3), by adding at the end the following: \u201cAny individual who participates in an intercollegiate sport for an institution of higher education, and is a student enrolled in the institution of higher education, shall be considered an employee of the institution of higher education if\u2014\n(A) the individual receives any form of direct compensation, including grant-in-aid, from the institution of higher education; and (B) any terms or conditions of such compensation require participation in an intercollegiate sport. ; and\n**(3)**\nby adding at the end the following:\n(15) The term grant-in-aid means a scholarship, grant, or other form of financial assistance that is provided by an institution of higher education to an individual for the individual\u2019s undergraduate or graduate course of study. (16) The term institution of higher education has the meaning given the term in section 102 of the Higher Education Act of 1965 ( 20 U.S.C. 1002 ). (17) The term intercollegiate athletic conference \u2014 (A) means any conference, or other group or organization, of institutions of higher education that\u2014 (i) exercises authority over intercollegiate sports at such institutions of higher education; and (ii) is engaged in commerce or an industry or activity affecting commerce; and (B) notwithstanding subparagraph (A), does not include the National Collegiate Athletic Association. (18) The term college athlete employee means an individual described in the second sentence of paragraph (3). .\n##### (b) Multiemployer bargaining unit\nSection 9(b) of the National Labor Relations Act ( 29 U.S.C. 159(b) ) is amended by striking the period at the end and inserting the following: : Provided , That, for the purpose of establishing an appropriate bargaining unit for college athlete employees at institutions of higher education in an intercollegiate athletic conference, the Board shall recognize multiple institutions of higher education within an intercollegiate athletic conference as a multiemployer bargaining unit, but only if consented to by the employee representatives for the intercollegiate sports bargaining units at the institutions of higher education that will be included in the multiemployer bargaining unit. .\n##### (c) Jurisdiction related to intercollegiate sports\nSection 14(c)(1) of the National Labor Relations Act ( 29 U.S.C. 164(c)(1) ) is amended by striking Provided , and inserting the following: Provided , That the Board shall exercise jurisdiction over institutions of higher education and college athlete employees of such institutions in relation to all collective bargaining matters under this Act pertaining to such employees, including any representation matter, such as recognizing or establishing a bargaining unit for such employees and any labor dispute involving such institutions and employees: Provided further , .\n##### (d) Prohibition on waiver\nAn individual may not enter into any agreement (including an agreement for grant-in-aid, as defined in section 2(15) of the National Labor Relations Act ( 29 U.S.C. 152(15) )) or legal settlement that waives or permits noncompliance with this Act or the amendments made by this Act.\n#### 4. Treatment of direct compensation for tax purposes and eligibility for Federal financial assistance\nNothing in this Act, or an amendment made by this Act, shall\u2014\n**(1)**\ncause any type of direct compensation described in section 2(3) of the National Labor Relations Act ( 29 U.S.C. 152(3) ) that was not previously treated as income for which a tax may be imposed under the Internal Revenue Code of 1986 to become a type of direct compensation for which such a tax may be imposed;\n**(2)**\ncause any individual to be treated as an employee, or cause any amounts received by an individual to be treated as wages, for purposes of any provision in the Internal Revenue Code of 1986 relating to employment taxes or the withholding of taxes by an employer if such individual or amounts would not otherwise be so treated;\n**(3)**\naffect the treatment of qualified scholarships under section 117 of the Internal Revenue Code of 1986; or\n**(4)**\notherwise affect the treatment of any direct compensation described in such section 2(3) in determining income, including gross income or adjusted gross income, for purposes of\u2014\n**(A)**\nthe Internal Revenue Code of 1986, including any reporting requirements under such Code; or\n**(B)**\ndetermining eligibility for any form of Federal financial assistance, including assistance under subpart 1 of part A of title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1070a et seq. ).\n#### 5. Severability\nIf any provision of this Act, an amendment made by this Act, or the application of such provision or amendment to any person or circumstance is held to be unconstitutional, the remainder of this Act and the amendments made by this Act, and the application of the provision or amendment to any other person or circumstance, shall not be affected.",
      "versionDate": "2025-07-28",
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
        "actionDate": "2025-07-23",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "4693",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "College Athlete Right to Organize Act",
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
        "name": "Labor and Employment",
        "updateDate": "2025-08-11T10:36:36Z"
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
      "date": "2025-07-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2469is.xml"
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
      "title": "College Athlete Right to Organize Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T04:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "College Athlete Right to Organize Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T04:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish collective bargaining rights for college athletes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T04:48:23Z"
    }
  ]
}
```
