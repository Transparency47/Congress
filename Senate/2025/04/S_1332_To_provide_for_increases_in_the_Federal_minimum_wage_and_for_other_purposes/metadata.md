# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1332?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1332
- Title: Raise the Wage Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1332
- Origin chamber: Senate
- Introduced date: 2025-04-08
- Update date: 2026-03-06T12:03:19Z
- Update date including text: 2026-03-06T12:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in Senate
- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-04-08: Introduced in Senate

## Actions

- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1332",
    "number": "1332",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "S000033",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Sanders, Bernard [I-VT]",
        "lastName": "Sanders",
        "party": "I",
        "state": "VT"
      }
    ],
    "title": "Raise the Wage Act of 2025",
    "type": "S",
    "updateDate": "2026-03-06T12:03:19Z",
    "updateDateIncludingText": "2026-03-06T12:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-08",
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
      "actionDate": "2025-04-08",
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
        "item": [
          {
            "date": "2025-04-08T16:39:10Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-08T16:39:10Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "MD"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "WI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "CT"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "DE"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NJ"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "WA"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
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
      "sponsorshipDate": "2025-04-08",
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
      "sponsorshipDate": "2025-04-08",
      "state": "PA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
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
      "sponsorshipDate": "2025-04-08",
      "state": "NY"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
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
      "sponsorshipDate": "2025-04-08",
      "state": "VA"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "AZ"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NJ"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "MN"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
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
      "sponsorshipDate": "2025-04-08",
      "state": "CT"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "WA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "CA"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
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
      "sponsorshipDate": "2025-04-08",
      "state": "RI"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
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
      "sponsorshipDate": "2025-04-08",
      "state": "CA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "MN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "MD"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
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
      "sponsorshipDate": "2025-04-08",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "VT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "RI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "OR"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "MI"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1332is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1332\nIN THE SENATE OF THE UNITED STATES\nApril 8, 2025 Mr. Sanders (for himself, Ms. Alsobrooks , Ms. Baldwin , Mr. Blumenthal , Ms. Blunt Rochester , Mr. Booker , Ms. Cantwell , Ms. Duckworth , Mr. Durbin , Mr. Fetterman , Mr. Gallego , Mrs. Gillibrand , Ms. Hirono , Mr. Kaine , Mr. Kelly , Mr. Kim , Ms. Klobuchar , Mr. Markey , Mr. Merkley , Mr. Murphy , Mrs. Murray , Mr. Padilla , Mr. Peters , Mr. Reed , Mr. Schatz , Mr. Schiff , Ms. Smith , Mr. Van Hollen , Mr. Warnock , Ms. Warren , Mr. Welch , Mr. Whitehouse , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo provide for increases in the Federal minimum wage, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Raise the Wage Act of 2025 .\n#### 2. Minimum wage increases\n##### (a) In general\nSection 6(a)(1) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206(a)(1) ) is amended to read as follows:\n(1) except as otherwise provided in this section, not less than\u2014 (A) $9.50 an hour, beginning on the effective date under section 7 of the Raise the Wage Act of 2025 ; (B) $11.00 an hour, beginning 1 year after such effective date; (C) $12.50 an hour, beginning 2 years after such effective date; (D) $14.00 an hour, beginning 3 years after such effective date; (E) $15.50 an hour, beginning 4 years after such effective date; (F) $17.00 an hour, beginning 5 years after such effective date; and (G) beginning on the date that is 6 years after such effective date, and annually thereafter, the amount determined by the Secretary under subsection (h); .\n##### (b) Determination based on increase in the median hourly wage of all employees\nSection 6 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206 ) is amended by adding at the end the following:\n(h) (1) Not later than each date that is 90 days before a new minimum wage determined under subsection (a)(1)(G) is to take effect, the Secretary shall determine the minimum wage to be in effect under this subsection for each period described in subsection (a)(1)(G). The wage determined under this subsection for a year shall be\u2014 (A) not less than the amount in effect under subsection (a)(1) on the date of such determination; (B) increased from such amount by the annual percentage increase, if any, in the median hourly wage of all employees as determined by the Bureau of Labor Statistics; and (C) rounded up to the nearest multiple of $0.05, if the amount after applying subparagraphs (A) and (B) is not a multiple of $0.05. (2) In calculating the annual percentage increase in the median hourly wage of all employees for purposes of paragraph (1)(B), the Secretary, through the Bureau of Labor Statistics, shall compile data on the hourly wages of all employees to determine such a median hourly wage and compare such median hourly wage for the most recent year for which data are available with the median hourly wage determined for the preceding year. .\n#### 3. Tipped employees\n##### (a) Base minimum wage for tipped employees and tips retained by employees\nSection 3(m)(2)(A)(i) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(m)(2)(A)(i) ) is amended to read as follows:\n(i) the cash wage paid such employee, which for purposes of such determination shall be not less than\u2014 (I) for the 1-year period beginning on the effective date under section 7 of the Raise the Wage Act of 2025 , $6.00 an hour; (II) $8.00 an hour, beginning 1 year after such effective date; (III) $10.00 an hour, beginning 2 years after such effective date; (IV) $12.00 an hour, beginning 3 years after such effective date; (V) $13.50 an hour, beginning 4 years after such effective date; (VI) $15.00 an hour, beginning 5 years after such effective date; (VII) $17.00 an hour, beginning 6 years after such effective date; and (VIII) for each succeeding 1-year period after the increase made pursuant to subclause (VII), the minimum wage in effect under section 6(a)(1); and .\n##### (b) Tips retained by employees\nSection 3(m)(2)(A) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(m)(2)(A) ) is amended\u2014\n**(1)**\nin the second sentence of the matter following clause (ii), by striking of this subsection, and all tips received by such employee have been retained by the employee and inserting of this subsection. Any employee shall have the right to retain any tips received by such employee ; and\n**(2)**\nby adding at the end the following: An employer shall inform each employee of the right and exception provided under the preceding sentence. .\n##### (c) Scheduled repeal of separate minimum wage for tipped employees\n**(1) Tipped employees**\nSection 3(m)(2)(A) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(m)(2)(A) ), as amended by subsections (a) and (b), is further amended by striking the sentence beginning with In determining the wage an employer is required to pay a tipped employee, and all that follows through of this subsection. and inserting The wage required to be paid to a tipped employee shall be the wage set forth in section 6(a)(1). .\n**(2) Publication of notice**\nSubsection (i) of section 6 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206 ), as added by section 5 and amended by section 6(b)(1), is further amended by striking or in accordance with subclause (II) or (III) of section 3(m)(2)(A)(i), .\n**(3) Effective date**\nThe amendments made by paragraphs (1) and (2) shall take effect on the date that is 1 day after the date on which the hourly wage under subclause (VIII) of section 3(m)(2)(A)(i) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(m)(2)(A)(i) ), as amended by subsection (a), takes effect.\n##### (d) Penalties\nSection 16 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 216 ) is amended\u2014\n**(1)**\nin the third sentence of subsection (b), by inserting or used after kept ; and\n**(2)**\nin the second sentence of subsection (e)(2), by inserting or used after kept .\n#### 4. Newly hired employees who are less than 20 years old\n##### (a) Base minimum wage for newly hired employees who are less than 20 years old\nSection 6(g)(1) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206(g)(1) ) is amended by striking a wage which is not less than $4.25 an hour. and inserting the following:\na wage at a rate that is not less than\u2014 (A) for the 1-year period beginning on the effective date under section 7 of the Raise the Wage Act of 2025 , $6.00 an hour; (B) for each succeeding 1-year period until the hourly wage under this paragraph equals the wage in effect under section 6(a)(1) for such period, an hourly wage equal to the amount determined under this paragraph for the preceding year, increased by the lesser of\u2014 (i) $1.75; or (ii) the amount necessary for the wage in effect under this paragraph to equal the wage in effect under section 6(a)(1) for such period; and (C) for each succeeding 1-year period after the increase made pursuant to subparagraph (B)(ii), the minimum wage in effect under section 6(a)(1). .\n##### (b) Scheduled repeal of separate minimum wage for newly hired employees who are less than 20 years old\n**(1) In general**\nSection 6(g) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206(g) ), as amended by subsection (a), shall be repealed.\n**(2) Publication of notice**\nSubsection (i) of section 6 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206 ), as added by section 5 and amended by sections 6(b)(1) and 3(c)(2), is further amended by striking or subparagraph (B) or (C) of subsection (g)(1) .\n**(3) Effective date**\nThe repeal and amendment made by paragraphs (1) and (2), respectively, shall take effect on the date that is 1 day after the date on which the hourly wage under subparagraph (C) of section 6(g)(1) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206(g)(1) ), as amended by subsection (a), takes effect.\n#### 5. Publication of notice\nSection 6 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206 ), as amended by section 2(b), is further amended by adding at the end the following:\n(i) Not later than 60 days prior to the effective date of any increase in the required wage determined under subsection (a)(1) or subparagraph (B) or (C) of subsection (g)(1), or in accordance with subclause (II) or (III) of section 3(m)(2)(A)(i) or section 14(c)(1)(A), the Secretary shall publish in the Federal Register and on the website of the Department of Labor a notice announcing each increase in such required wage. .\n#### 6. Promoting economic self-sufficiency for individuals with disabilities\n##### (a) Wages\n**(1) Transition to fair wages for individuals with disabilities**\nSubparagraph (A) of section 14(c)(1) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 214(c)(1) ) is amended to read as follows:\n(A) at a rate that equals or exceeds, for each year, the greater of\u2014 (i) (I) $5.00 an hour, beginning on the effective date under section 7 of the Raise the Wage Act of 2025 ; (II) $7.50 an hour, beginning 1 year after such effective date; (III) $10.00 an hour, beginning 2 years after such effective date; (IV) $12.50 an hour, beginning 3 years after such effective date; (V) $15.50 an hour, beginning 4 years after such effective date; and (VI) the wage rate in effect under section 6(a)(1), beginning 5 years after such effective date; or (ii) if applicable, the wage rate in effect on the day before the date of enactment of the Raise the Wage Act of 2025 for the employment, under a special certificate issued under this paragraph, of the individual for whom the wage rate is being determined under this subparagraph, .\n**(2) Prohibition on new special certificates; transition assistance**\n**(A) In general**\nSection 14(c) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 214(c) ) is amended by adding at the end the following:\n(6) Prohibition on new special certificates Notwithstanding paragraph (1), the Secretary shall not issue a special certificate under this subsection to an employer that was not issued a special certificate under this subsection before the date of enactment of the Raise the Wage Act of 2025 . (7) Transition assistance Upon request, the Secretary shall provide\u2014 (A) technical assistance and information to employers issued a special certificate under this subsection for the purposes of\u2014 (i) assisting such employers to comply with this subsection, as amended by the Raise the Wage Act of 2025 ; and (ii) ensuring continuing employment opportunities for individuals with disabilities receiving a special minimum wage rate under this subsection; and (B) information to individuals employed at a special minimum wage rate under this subsection, which may include referrals to Federal or State entities with expertise in competitive integrated employment. .\n**(B) Effective date**\nThe amendments made by this paragraph shall take effect on the date of enactment of this Act.\n**(3) Sunset**\nSection 14(c) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 214(c) ), as amended by paragraph (2), is further amended by adding at the end the following:\n(8) Sunset Beginning on the day after the date on which the wage rate described in paragraph (1)(A)(i)(VI) takes effect, the authority to issue special certificates under paragraph (1) shall expire, and no special certificates issued under paragraph (1) shall have any legal effect. .\n##### (b) Publication of notice\n**(1) Amendment**\nSubsection (i) of section 6 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206 ), as added by section 5, is amended by striking or section 14(c)(1)(A) .\n**(2) Effective date**\nThe amendment made by paragraph (1) shall take effect on the day after the date on which the wage rate described in paragraph (1)(A)(i)(VI) of section 14(c) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 214(c) ), as amended by subsection (a)(1), takes effect.\n#### 7. General effective date\nExcept as otherwise provided in this Act, this Act and the amendments made by this Act shall take effect on the first day of the third month that begins after the date of the enactment of this Act.",
      "versionDate": "2025-04-08",
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
        "actionDate": "2025-04-08",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "2743",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Raise the Wage Act of 2025",
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
        "updateDate": "2025-05-05T13:56:36Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1332is.xml"
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
      "title": "Raise the Wage Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-06T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Raise the Wage Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-23T02:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for increases in the Federal minimum wage, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-23T02:48:19Z"
    }
  ]
}
```
