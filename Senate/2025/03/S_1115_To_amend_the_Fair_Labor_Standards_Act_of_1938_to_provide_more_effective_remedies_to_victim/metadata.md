# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1115?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1115
- Title: Paycheck Fairness Act
- Congress: 119
- Bill type: S
- Bill number: 1115
- Origin chamber: Senate
- Introduced date: 2025-03-25
- Update date: 2025-04-21T12:24:17Z
- Update date including text: 2025-04-21T12:24:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in Senate
- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-03-25: Introduced in Senate

## Actions

- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1115",
    "number": "1115",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "M001111",
        "district": "",
        "firstName": "Patty",
        "fullName": "Sen. Murray, Patty [D-WA]",
        "lastName": "Murray",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Paycheck Fairness Act",
    "type": "S",
    "updateDate": "2025-04-21T12:24:17Z",
    "updateDateIncludingText": "2025-04-21T12:24:17Z"
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
          "date": "2025-03-25T19:08:55Z",
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
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-03-25",
      "state": "VT"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "MD"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "WI"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "CO"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "CT"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "DE"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NJ"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "WA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "DE"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NV"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "IL"
    },
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
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "PA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "AZ"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NY"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NH"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NM"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "CO"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "HI"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "VA"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "AZ"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NJ"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-03-25",
      "state": "ME"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "MN"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Lujan",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NM"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "OR"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "CT"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "GA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "MI"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "RI"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NV"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "HI"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NY"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NH"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "MI"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "MN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "MD"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "VA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "GA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "MA"
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
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "RI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1115is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1115\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2025 Mrs. Murray (for herself, Mr. Sanders , Ms. Alsobrooks , Ms. Baldwin , Mr. Bennet , Mr. Blumenthal , Ms. Blunt Rochester , Mr. Booker , Ms. Cantwell , Mr. Coons , Ms. Cortez Masto , Ms. Duckworth , Mr. Durbin , Mr. Fetterman , Mr. Gallego , Mrs. Gillibrand , Ms. Hassan , Mr. Heinrich , Mr. Hickenlooper , Ms. Hirono , Mr. Kaine , Mr. Kelly , Mr. Kim , Mr. King , Ms. Klobuchar , Mr. Luj\u00e1n , Mr. Markey , Mr. Merkley , Mr. Murphy , Mr. Ossoff , Mr. Padilla , Mr. Peters , Mr. Reed , Ms. Rosen , Mr. Schatz , Mr. Schiff , Mr. Schumer , Mrs. Shaheen , Ms. Slotkin , Ms. Smith , Mr. Van Hollen , Mr. Warner , Mr. Warnock , Ms. Warren , Mr. Welch , Mr. Whitehouse , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Fair Labor Standards Act of 1938 to provide more effective remedies to victims of discrimination in the payment of wages on the basis of sex, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Paycheck Fairness Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nWomen have entered the workforce in record numbers over the past 50 years.\n**(2)**\nDespite the enactment of the Equal Pay Act of 1963 ( Public Law 88\u201338 ), many women continue to earn significantly lower pay than men for equal work. These pay disparities exist in both the private and governmental sectors. Pay disparities are especially severe for women and girls of color.\n**(3)**\nIn many instances, the pay disparities can only be due to continued intentional discrimination or the lingering effects of past discrimination. After controlling for educational attainment, occupation, industry, union status, race, ethnicity, and labor force experience roughly 40 percent of the pay gap remains unexplained.\n**(4)**\nThe existence of such pay disparities\u2014\n**(A)**\ndepresses the wages of working families who rely on the wages of all members of the family to make ends meet;\n**(B)**\nundermines women's retirement security, which is often based on earnings while in the workforce;\n**(C)**\nprevents women from realizing their full economic potential, particularly in terms of labor force participation and attachment;\n**(D)**\nhas been spread and perpetuated, through commerce and the channels and instrumentalities of commerce, among the workers of the several States;\n**(E)**\nburdens commerce and the free flow of goods in commerce;\n**(F)**\nconstitutes an unfair method of competition in commerce;\n**(G)**\ntends to cause labor disputes, as evidenced by the tens of thousands of charges filed with the Equal Employment Opportunity Commission against employers between 2010 and 2016;\n**(H)**\ninterferes with the orderly and fair marketing of goods in commerce; and\n**(I)**\nin many instances, may deprive workers of equal protection on the basis of sex in violation of the Fifth and 14th Amendments to the Constitution of the United States.\n**(5)**\n**(A)**\nArtificial barriers to the elimination of discrimination in the payment of wages on the basis of sex continue to exist decades after the enactment of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 201 et seq. ) and the Civil Rights Act of 1964 ( 42 U.S.C. 2000a et seq. ).\n**(B)**\nThese barriers have resulted, in significant part, because the Equal Pay Act of 1963 has not worked as Congress originally intended. Improvements and modifications to the law are necessary to ensure that the Act provides effective protection to those subject to pay discrimination on the basis of their sex.\n**(C)**\nElimination of such barriers would have positive effects, including\u2014\n**(i)**\nproviding a solution to problems in the economy created by unfair pay disparities;\n**(ii)**\nsubstantially reducing the number of working women earning unfairly low wages, thereby reducing the dependence on public assistance;\n**(iii)**\npromoting stable families by enabling all family members to earn a fair rate of pay;\n**(iv)**\nremedying the effects of past discrimination on the basis of sex and ensuring that in the future workers are afforded equal protection on the basis of sex; and\n**(v)**\nensuring equal protection pursuant to Congress\u2019 power to enforce the Fifth and 14th Amendments to the Constitution of the United States.\n**(6)**\nThe Department of Labor and the Equal Employment Opportunity Commission carry out functions to help ensure that women receive equal pay for equal work.\n**(7)**\nThe Department of Labor is responsible for\u2014\n**(A)**\ncollecting and making publicly available information about women\u2019s pay;\n**(B)**\ndisseminating information about women\u2019s rights in the workplace;\n**(C)**\nhelping women who have been victims of pay discrimination obtain a remedy; and\n**(D)**\ninvestigating and prosecuting systemic gender based pay discrimination involving government contractors.\n**(8)**\nThe Equal Employment Opportunity Commission is the primary enforcement agency for claims made under the Equal Pay Act of 1963, and issues regulations and guidance on appropriate interpretations of the law.\n**(9)**\nVigorous implementation by the Department of Labor and the Equal Employment Opportunity Commission, increased information as a result of the amendments made by this Act, wage data, and more effective remedies, will ensure that women are better able to recognize and enforce their rights.\n**(10)**\nCertain employers have already made great strides in eradicating unfair pay disparities in the workplace and their achievements should be recognized.\n#### 3. Enhanced enforcement of equal pay requirements\n##### (a) Bona Fide factor defense and modification of same establishment requirement\nSection 6(d)(1) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206(d)(1) ) is amended\u2014\n**(1)**\nby striking No employer having and inserting (A) No employer having ;\n**(2)**\nby striking any other factor other than sex and inserting a bona fide factor other than sex, such as education, training, or experience ; and\n**(3)**\nby adding at the end the following:\n(B) The bona fide factor defense described in subparagraph (A)(iv) shall apply only if the employer demonstrates that such factor (i) is not based upon or derived from a sex-based differential in compensation; (ii) is job-related with respect to the position in question; (iii) is consistent with business necessity; and (iv) accounts for the entire differential in compensation at issue. Such defense shall not apply where the employee demonstrates that an alternative employment practice exists that would serve the same business purpose without producing such differential and that the employer has refused to adopt such alternative practice. (C) For purposes of subparagraph (A), employees shall be deemed to work in the same establishment if the employees work for the same employer at workplaces located in the same county or similar political subdivision of a State. The preceding sentence shall not be construed as limiting broader applications of the term establishment consistent with rules prescribed or guidance issued by the Equal Employment Opportunity Commission. .\n##### (b) Nonretaliation provision\nSection 15 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 215 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (3), by striking employee has filed and all that follows and inserting\nemployee\u2014 (A) has made a charge or filed any complaint or instituted or caused to be instituted any investigation, proceeding, hearing, or action under or related to this Act, including an investigation conducted by the employer, or has testified or is planning to testify or has assisted or participated in any manner in any such investigation, proceeding, hearing or action, or has served or is planning to serve on an industry committee; or (B) has inquired about, discussed, or disclosed the wages of the employee or another employee (such as by inquiring or discussing with the employer why the wages of the employee involved are set at a certain rate or salary); ;\n**(B)**\nin paragraph (5), by striking and at the end;\n**(C)**\nin paragraph (6), by striking the period at the end and inserting ; and ; and\n**(D)**\nby adding at the end the following:\n(7) to require an employee to sign a contract or waiver that would prohibit the employee from disclosing information about the employee\u2019s wages. ; and\n**(2)**\nby adding at the end the following:\n(c) Subsection (a)(3)(B) shall not apply to instances in which an employee who has access to the wage information of other employees as a part of such employee\u2019s essential job functions discloses the wages of such other employees to individuals who do not otherwise have access to such information, unless such disclosure is in response to a complaint or charge or in furtherance of an investigation, proceeding, hearing, or action under section 6(d), including an investigation conducted by the employer. Nothing in this subsection shall be construed to limit the rights of an employee provided under any other provision of law. .\n##### (c) Enhanced penalties\nSection 16(b) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 216(b) ) is amended\u2014\n**(1)**\nby inserting after the first sentence the following: Any employer who violates section 6(d) shall additionally be liable for such compensatory damages, or, if the employee demonstrates that the employer acted with malice or reckless indifference, punitive damages as may be appropriate, except that the United States shall not be liable for punitive damages. ;\n**(2)**\nin the sentence beginning An action to , by striking the preceding sentences and inserting any of the preceding sentences of this subsection ;\n**(3)**\nin the sentence beginning No employees shall , by striking No employees and inserting Except with respect to class actions brought to enforce section 6(d), no employee ;\n**(4)**\nby inserting after the sentence referred to in paragraph (3), the following: Notwithstanding any other provision of Federal law, any action brought to enforce section 6(d) may be maintained as a class action as provided by the Federal Rules of Civil Procedure. ; and\n**(5)**\nin the sentence beginning The court in \u2014\n**(A)**\nby striking in such action and inserting in any action brought to recover the liability prescribed in any of the preceding sentences of this subsection ; and\n**(B)**\nby inserting before the period the following: , including expert fees .\n##### (d) Action by the Secretary\nSection 16(c) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 216(c) ) is amended\u2014\n**(1)**\nin the first sentence\u2014\n**(A)**\nby inserting or, in the case of a violation of section 6(d), additional compensatory or punitive damages, as described in subsection (b), before and the agreement ; and\n**(B)**\nby inserting before the period the following: , or such compensatory or punitive damages, as appropriate ;\n**(2)**\nin the second sentence, by inserting before the period the following: and, in the case of a violation of section 6(d), additional compensatory or punitive damages, as described in subsection (b) ;\n**(3)**\nin the third sentence, by striking the first sentence and inserting the first or second sentence ; and\n**(4)**\nin the sixth sentence\u2014\n**(A)**\nby striking commenced in the case and inserting\ncommenced\u2014 (1) in the case ;\n**(B)**\nby striking the period and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(2) in the case of a class action brought to enforce section 6(d), on the date on which the individual becomes a party plaintiff to the class action. .\n#### 4. Training\nThe Equal Employment Opportunity Commission and the Office of Federal Contract Compliance Programs, subject to the availability of funds appropriated under section 11, shall provide training to Commission employees and affected individuals and entities on matters involving discrimination in the payment of wages.\n#### 5. Negotiation skills training\n##### (a) Program authorized\n**(1) In general**\nThe Secretary of Labor, after consultation with the Secretary of Education, is authorized to establish and carry out a grant program.\n**(2) Grants**\nIn carrying out the program, the Secretary of Labor may make grants on a competitive basis to eligible entities to carry out negotiation skills training programs for the purposes of addressing pay disparities, including through outreach to women and girls.\n**(3) Eligible entities**\nTo be eligible to receive a grant under this subsection, an entity shall be a public agency, such as a State, a local government in a metropolitan statistical area (as defined by the Office of Management and Budget), a State educational agency, or a local educational agency, a private nonprofit organization, or a community-based organization.\n**(4) Application**\nTo be eligible to receive a grant under this subsection, an entity shall submit an application to the Secretary of Labor at such time, in such manner, and containing such information as the Secretary of Labor may require.\n**(5) Use of funds**\nAn entity that receives a grant under this subsection shall use the funds made available through the grant to carry out an effective negotiation skills training program for the purposes described in paragraph (2).\n##### (b) Incorporating training into existing programs\nThe Secretary of Labor and the Secretary of Education shall issue regulations or policy guidance that provides for integrating the negotiation skills training, to the extent practicable, into programs authorized under\u2014\n**(1)**\nin the case of the Secretary of Education, the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6301 et seq. ), the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2301 et seq. ), the Higher Education Act of 1965 ( 20 U.S.C. 1001 et seq. ), and other programs carried out by the Department of Education that the Secretary of Education determines to be appropriate; and\n**(2)**\nin the case of the Secretary of Labor, the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3101 et seq. ), and other programs carried out by the Department of Labor that the Secretary of Labor determines to be appropriate.\n##### (c) Report\nNot later than 18 months after the date of enactment of this Act, and annually thereafter, the Secretary of Labor, in consultation with the Secretary of Education, shall prepare and submit to Congress a report describing the activities conducted under this section and evaluating the effectiveness of such activities in achieving the purposes of this section.\n#### 6. Research, education, and outreach\n##### (a) In general\nNot later than 18 months after the date of enactment of this Act, and periodically thereafter, the Secretary of Labor shall conduct studies and provide information to employers, labor organizations, and the general public concerning the means available to eliminate pay disparities between men and women (including women who are Asian American, Black or African American, Hispanic American or Latino, Native American or Alaska Native, Native Hawaiian or Pacific Islander, and White American), including\u2014\n**(1)**\nconducting and promoting research to develop the means to correct expeditiously the conditions leading to the pay disparities, with specific attention paid to women and girls from historically underrepresented and minority groups;\n**(2)**\npublishing and otherwise making available to employers, labor organizations, professional associations, educational institutions, the media, and the general public the findings resulting from studies and other materials, relating to eliminating the pay disparities;\n**(3)**\nsponsoring and assisting State, local, and community informational and educational programs;\n**(4)**\nproviding information to employers, labor organizations, professional associations, and other interested persons on the means of eliminating the pay disparities; and\n**(5)**\nrecognizing and promoting the achievements of employers, labor organizations, and professional associations that have worked to eliminate the pay disparities.\n##### (b) Report on gender pay gap in teenage labor force\n**(1) Report required**\nNot later than one year after the date of the enactment of this Act, the Secretary of Labor, acting through the Director of the Women\u2019s Bureau and in coordination with the Commissioner of Labor Statistics, shall\u2014\n**(A)**\nsubmit to Congress a report on the gender pay gap in the teenage labor force; and\n**(B)**\nmake the report available on a publicly accessible website of the Department of Labor.\n**(2) Elements**\nThe report under paragraph (1) shall include the following:\n**(A)**\nAn examination of trends and potential solutions relating to the teenage gender pay gap.\n**(B)**\nAn examination of how the teenage gender pay gap potentially translates into greater wage gaps in the overall labor force.\n**(C)**\nAn examination of overall lifetime earnings and losses for informal and formal jobs for women, including women of color.\n**(D)**\nAn examination of the teenage gender pay gap, including a comparison of the average amount earned by males and females, respectively, in informal jobs, such as babysitting and other freelance jobs, as well as formal jobs, such as retail, restaurant, and customer service.\n**(E)**\nA comparison of\u2014\n**(i)**\nthe types of tasks typically performed by women from the teenage years through adulthood within certain informal jobs, such as babysitting and other freelance jobs, and formal jobs, such as retail, restaurant, and customer service; and\n**(ii)**\nthe types of tasks performed by younger males in such positions.\n**(F)**\nInterviews and surveys with workers and employers relating to early gender-based pay discrepancies.\n**(G)**\nRecommendations for\u2014\n**(i)**\naddressing pay inequality for women from the teenage years through adulthood, including such women of color;\n**(ii)**\naddressing any disadvantages experienced by young women with respect to work experience and professional development;\n**(iii)**\nthe development of standards and best practices for workers and employees to ensure better pay for young women and the prevention of early inequalities in the workplace; and\n**(iv)**\nexpanding awareness for teenage girls on pay rates and employment rights in order to reduce greater inequalities in the overall labor force.\n#### 7. Establishment of the National Award for Pay Equity in the Workplace\n##### (a) In general\nThere is established the Secretary of Labor\u2019s National Award for Pay Equity in the Workplace, which shall be awarded, on an annual basis, to an employer to encourage proactive efforts to comply with section 6(d) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206(d) ), as amended by this Act.\n##### (b) Criteria for qualification\nThe Secretary of Labor shall set criteria for receipt of the award, including a requirement that an employer has made substantial effort to eliminate pay disparities between men and women, and deserves special recognition as a consequence of such effort. The Secretary shall establish procedures for the application and presentation of the award.\n##### (c) Business\nIn this section, the term employer includes\u2014\n**(1)**\n**(A)**\na corporation, including a nonprofit corporation;\n**(B)**\na partnership;\n**(C)**\na professional association;\n**(D)**\na labor organization; and\n**(E)**\na business entity similar to an entity described in any of subparagraphs (A) through (D);\n**(2)**\nan entity carrying out an education referral program, a training program, such as an apprenticeship or management training program, or a similar program; and\n**(3)**\nan entity carrying out a joint program, formed by a combination of any entities described in paragraph (1) or (2).\n#### 8. Collection of pay information by the equal employment opportunity Commission\nSection 709 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e\u20138 ) is amended by adding at the end the following:\n(f) (1) Not later than 18 months after the date of enactment of this subsection, the Commission shall provide for the collection from employers of compensation data and other employment-related data (including hiring, termination, and promotion data) disaggregated by the sex, race, and ethnic identity of employees. (2) In carrying out paragraph (1), the Commission shall have as its primary consideration the most effective and efficient means for enhancing the enforcement of Federal laws prohibiting pay discrimination. For this purpose, the Commission shall consider factors including the imposition of burdens on employers, the frequency of required reports (including the size of employers required to prepare reports), appropriate protections for maintaining data confidentiality, and the most effective format to report such data. (3) (A) For each 12-month reporting period for an employer, the compensation data collected under paragraph (1) shall include, for each range of taxable compensation described in subparagraph (B), disaggregated by the categories described in subparagraph (E)\u2014 (i) the number of employees of the employer who earn taxable compensation in an amount that falls within such taxable compensation range; and (ii) the total number of hours worked by such employees. (B) Subject to adjustment under subparagraph (C), the taxable compensation ranges described in this subparagraph are as follows: (i) Not more than $19,239. (ii) Not less than $19,240 and not more than $24,439. (iii) Not less than $24,440 and not more than $30,679. (iv) Not less than $30,680 and not more than $38,999. (v) Not less than $39,000 and not more than $49,919. (vi) Not less than $49,920 and not more than $62,919. (vii) Not less than $62,920 and not more than $80,079. (viii) Not less than $80,080 and not more than $101,919. (ix) Not less than $101,920 and not more than $128,959. (x) Not less than $128,960 and not more than $163,799. (xi) Not less than $163,800 and not more than $207,999. (xii) Not less than $208,000. (C) The Commission may adjust the taxable compensation ranges under subparagraph (B)\u2014 (i) if the Commission determines that such adjustment is necessary to enhance enforcement of Federal laws prohibiting pay discrimination; or (ii) for inflation, in consultation with the Bureau of Labor Statistics. (D) In collecting data described in subparagraph (A)(ii), the Commission shall provide that, with respect to an employee who the employer is not required to compensate for overtime employment under section 7 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 207 ), an employer may report\u2014 (i) in the case of a full-time employee, that such employee works 40 hours per week, and in the case of a part-time employee, that such employee works 20 hours per week; or (ii) the actual number of hours worked by such employee. (E) The categories described in this subparagraph shall be determined by the Commission and shall include\u2014 (i) race; (ii) ethnic identity; (iii) sex; and (iv) job categories, including the job categories described in the instructions for the Equal Employment Opportunity Employer Information Report EEO\u20131, as in effect on the date of the enactment of this subsection. (F) The Commission shall use the compensation data collected under paragraph (1)\u2014 (i) to enhance\u2014 (I) the investigation of charges filed under section 706 or section 6(d) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206(d) ); and (II) the allocation of resources to investigate such charges; and (ii) for any other purpose that the Commission determines appropriate. (G) The Commission shall annually make publicly available aggregate compensation data collected under paragraph (1) for the categories described in subparagraph (E), disaggregated by industry, occupation, and core based statistical area (as defined by the Office of Management and Budget). (4) The compensation data under paragraph (1) shall be collected from each employer that\u2014 (A) is a private employer that has 100 or more employees, including such an employer that is a contractor with the Federal Government, or a subcontractor at any tier thereof; or (B) the Commission determines appropriate. .\n#### 9. Reinstatement of pay equity programs and pay equity data collection\n##### (a) Bureau of Labor Statistics data collection\nThe Commissioner of Labor Statistics shall continue to collect data on women workers in the Current Employment Statistics survey.\n##### (b) Office of Federal Contract Compliance Programs initiatives\nThe Director of the Office of Federal Contract Compliance Programs shall ensure that employees of the Office\u2014\n**(1)**\n**(A)**\nshall use the full range of investigatory tools at the Office's disposal, including pay grade methodology;\n**(B)**\nin considering evidence of possible compensation discrimination\u2014\n**(i)**\nshall not limit its consideration to a small number of types of evidence; and\n**(ii)**\nshall not limit its evaluation of the evidence to a small number of methods of evaluating the evidence; and\n**(C)**\nshall not require a multiple regression analysis or anecdotal evidence for a compensation discrimination case;\n**(2)**\nfor purposes of its investigative, compliance, and enforcement activities, shall define similarly situated employees in a way that is consistent with and not more stringent than the definition provided in item 1 of subsection A of section 10\u2013III of the Equal Employment Opportunity Commission Compliance Manual (2000), and shall consider only factors that the Office's investigation reveals were used in making compensation decisions; and\n**(3)**\nshall implement a survey to collect compensation data and other employment-related data (including hiring, termination, and promotion data) and designate not less than half of all nonconstruction contractor establishments each year to prepare and file such survey, and shall review and utilize the responses to such survey to identify contractor establishments for further evaluation and for other enforcement purposes as appropriate.\n##### (c) Department of Labor distribution of wage discrimination information\nThe Secretary of Labor shall make readily available (in print, on the Department of Labor website, and through any other forum that the Department may use to distribute compensation discrimination information), accurate information on compensation discrimination, including statistics, explanations of employee rights, historical analyses of such discrimination, instructions for employers on compliance, and any other information that will assist the public in understanding and addressing such discrimination.\n#### 10. Prohibitions relating to prospective employees\u2019 salary and benefit history\n##### (a) In general\nThe Fair Labor Standards Act of 1938 ( 29 U.S.C. 201 et seq. ) is amended by inserting after section 7 the following new section:\n8. Requirements and prohibitions relating to wage, salary, and benefit history (a) In general It shall be an unlawful practice for an employer to\u2014 (1) rely on the wage history of a prospective employee in considering the prospective employee for employment in a position as an employee who in any workweek is engaged in commerce or in the production of goods for commerce, or is employed in an enterprise engaged in commerce or in the production of goods for commerce, including requiring that a prospective employee\u2019s prior wages satisfy minimum or maximum criteria as a condition of being considered for such employment; (2) rely on the wage history of a prospective employee in determining the wages for such prospective employee for a position described in paragraph (1) of the employer, except that an employer may rely on wage history if it is voluntarily provided by a prospective employee, after the employer makes an offer of employment in such a position with an offer of compensation to the prospective employee for such position, to support a wage higher than the wage offered by the employer; (3) seek from a prospective employee for a position described in paragraph (1) or any current or former employer of such prospective employee the wage history of the prospective employee, except that an employer may seek to confirm prior wage information only after an offer of employment for such a position with compensation has been made to the prospective employee and the prospective employee responds to the offer by providing prior wage information to support a wage higher than that offered by the employer; or (4) discharge or in any other manner retaliate against any employee or prospective employee for a position described in paragraph (1) because the employee or prospective employee\u2014 (A) opposed any act or practice made unlawful by this section; or (B) took an action for which discrimination is forbidden under section 15(a)(3). (b) Definition In this section, the term wage history means the wages paid to the prospective employee by the prospective employee\u2019s current employer or previous employer. .\n##### (b) Penalties\nSection 16 of such Act ( 29 U.S.C. 216 ) is amended by adding at the end the following new subsection:\n(f) (1) Any person who violates the provisions of section 8 shall\u2014 (A) be subject to a civil penalty of $5,000 for a first offense, increased by an additional $1,000 for each subsequent offense, not to exceed $10,000; and (B) be liable to each employee or prospective employee who was the subject of the violation for special damages not to exceed $10,000 plus attorneys\u2019 fees, and shall be subject to such injunctive relief as may be appropriate. (2) An action to recover the liability described in paragraph (1)(B) may be maintained against any employer (including a public agency) in any Federal or State court of competent jurisdiction by any one or more employees or prospective employees for and on behalf of\u2014 (A) the employees or prospective employees; and (B) other employees or prospective employees similarly situated. .\n##### (c) Conforming amendment\nSection 10 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 210 ) is repealed.\n#### 11. Authorization of appropriations\n##### (a) Authorization of Appropriations\nThere are authorized to be appropriated such sums as may be necessary to carry out this Act.\n##### (b) Prohibition on Earmarks\nNone of the funds appropriated pursuant to subsection (a) for purposes of the grant program in section 5 of this Act may be used for a congressional earmark as defined in clause 9(e) of rule XXI of the Rules of the House of Representatives.\n#### 12. Small Business Assistance\n##### (a) Effective date\nThis Act and the amendments made by this Act shall take effect on the date that is 6 months after the date of enactment of this Act.\n##### (b) Technical assistance materials\nThe Secretary of Labor and the Commissioner of the Equal Employment Opportunity Commission shall jointly develop technical assistance material to assist small enterprises in complying with the requirements of this Act and the amendments made by this Act.\n##### (c) Small Businesses\nA small enterprise shall be exempt from the provisions of this Act, and the amendments made by this Act, to the same extent that such enterprise is exempt from the requirements of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 201 et seq. ) pursuant to clauses (i) and (ii) of section 3(s)(1)(A) of such Act ( 29 U.S.C. 203(s)(1)(A) ).\n#### 13. Rule of Construction\nNothing in this Act, or in any amendments made by this Act, shall affect the obligation of employers and employees to fully comply with all applicable immigration laws, including being subject to any penalties, fines, or other sanctions.\n#### 14. Severability\nIf any provision of this Act, an amendment made by this Act, or the application of that provision or amendment to particular persons or circumstances is held invalid or found to be unconstitutional, the remainder of this Act, the amendments made by this Act, or the application of that provision to other persons or circumstances shall not be affected.",
      "versionDate": "2025-03-25",
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
        "actionDate": "2025-03-18",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "2219",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Salary History Question Prohibition Act",
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
        "updateDate": "2025-04-03T17:13:14Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1115is.xml"
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
      "title": "Paycheck Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Paycheck Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Fair Labor Standards Act of 1938 to provide more effective remedies to victims of discrimination in the payment of wages on the basis of sex, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:27Z"
    }
  ]
}
```
