# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1663?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1663
- Title: Therapeutic Fraud Prevention Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1663
- Origin chamber: Senate
- Introduced date: 2025-05-07
- Update date: 2025-12-05T21:32:33Z
- Update date including text: 2025-12-05T21:32:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in Senate
- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-05-07: Introduced in Senate

## Actions

- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1663",
    "number": "1663",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
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
    "title": "Therapeutic Fraud Prevention Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:32:33Z",
    "updateDateIncludingText": "2025-12-05T21:32:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-07",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-07",
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
          "date": "2025-05-07T21:23:13Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "NJ"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "WI"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "CO"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "CT"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
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
      "sponsorshipDate": "2025-05-07",
      "state": "DE"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "NV"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
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
      "sponsorshipDate": "2025-05-07",
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
      "sponsorshipDate": "2025-05-07",
      "state": "PA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "NY"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "NH"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
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
      "sponsorshipDate": "2025-05-07",
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
      "sponsorshipDate": "2025-05-07",
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
      "sponsorshipDate": "2025-05-07",
      "state": "VA"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "AZ"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
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
      "sponsorshipDate": "2025-05-07",
      "state": "ME"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "MN"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
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
      "sponsorshipDate": "2025-05-07",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
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
      "sponsorshipDate": "2025-05-07",
      "state": "CT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "CA"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "RI"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "NV"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-05-07",
      "state": "VT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "CA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "NH"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "MI"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "MN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "MD"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "VT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "RI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "OR"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-05-12",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1663is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1663\nIN THE SENATE OF THE UNITED STATES\nMay 7, 2025 Mrs. Murray (for herself, Mr. Booker , Ms. Baldwin , Mr. Bennet , Mr. Blumenthal , Ms. Cantwell , Mr. Coons , Ms. Cortez Masto , Ms. Duckworth , Mr. Durbin , Mr. Fetterman , Mrs. Gillibrand , Ms. Hassan , Mr. Heinrich , Mr. Hickenlooper , Ms. Hirono , Mr. Kaine , Mr. Kelly , Mr. Kim , Mr. King , Ms. Klobuchar , Mr. Luj\u00e1n , Mr. Markey , Mr. Merkley , Mr. Murphy , Mr. Padilla , Mr. Reed , Ms. Rosen , Mr. Sanders , Mr. Schiff , Mrs. Shaheen , Ms. Slotkin , Ms. Smith , Mr. Van Hollen , Ms. Warren , Mr. Welch , Mr. Whitehouse , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo prohibit commercial sexual orientation conversion therapy, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Therapeutic Fraud Prevention Act of 2025 .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nBeing lesbian, gay, bisexual, transgender, or gender nonconforming is not a disorder, disease, illness, deficiency, or shortcoming.\n**(2)**\nThe national community of professionals in education, social work, health, mental health, and counseling has determined that there is no scientifically valid evidence that supports the practice of attempting to prevent a person from being lesbian, gay, bisexual, transgender, or gender nonconforming.\n**(3)**\nSuch professionals have determined that there is no evidence that conversion therapy is effective or that an individual\u2019s sexual orientation or gender identity can be changed by conversion therapy.\n**(4)**\nSuch professionals have also determined that the potential risks of conversion therapy are not only that it is ineffective, but also that it is substantially dangerous to an individual\u2019s mental and physical health, and has been shown to contribute to depression, self-harm, low self-esteem, family rejection, and suicide.\n**(5)**\nIt is in the interest of the Nation to prevent lesbian, gay, bisexual, transgender, and gender nonconforming people and their families from being defrauded by persons seeking to profit by offering this harmful and wholly ineffective therapy.\n#### 3. Definitions\nIn this Act:\n**(1) Conversion therapy**\nThe term conversion therapy \u2014\n**(A)**\nmeans any practice or treatment by any person that seeks to change another individual\u2019s sexual orientation or gender identity, including efforts to change behaviors or gender expressions, or to eliminate or reduce sexual or romantic attractions or feelings toward individuals of the same gender, if such person\u2014\n**(i)**\nreceives monetary compensation in exchange for such practice or treatment; or\n**(ii)**\ninstead of, or in addition to, receiving monetary compensation in exchange for such practice or treatment directly, receives monetary compensation in exchange for a product or service that is integral to the provision of such practice or treatment by such person, unless such product or service is protected by the First Amendment to the Constitution; and\n**(B)**\ndoes not include any practice or treatment, which does not seek to change sexual orientation or gender identity, that\u2014\n**(i)**\nprovides assistance to an individual undergoing a gender transition; or\n**(ii)**\nprovides acceptance, support, and understanding of a client or facilitation of a client\u2019s coping, social support, and identity exploration and development, including sexual orientation-neutral interventions to prevent or address unlawful conduct or unsafe sexual practices.\n**(2) Gender identity**\nThe term gender identity means the gender-related identity, appearance, mannerisms, or other gender-related characteristics of an individual, regardless of the individual\u2019s designated sex at birth.\n**(3) Person**\nThe term person means any individual, partnership, corporation, cooperative, association, or any other entity.\n**(4) Sexual orientation**\nThe term sexual orientation means homosexuality, heterosexuality, or bisexuality.\n#### 4. Unlawful conduct related to conversion therapy\n##### (a) In general\nIt shall be unlawful for any person\u2014\n**(1)**\nto provide conversion therapy to any individual;\n**(2)**\nto advertise for the provision of conversion therapy and claim in such advertising\u2014\n**(A)**\nto change another individual\u2019s sexual orientation or gender identity;\n**(B)**\nto eliminate or reduce sexual or romantic attractions or feelings toward individuals of the same gender; or\n**(C)**\nthat such efforts are harmless or without risk to individuals receiving such therapy; or\n**(3)**\nto knowingly assist or facilitate the provision of conversion therapy to an individual if such person receives compensation from any source in connection with providing conversion therapy.\n##### (b) Enforcement by Federal Trade Commission\n**(1) Violation of rule**\nA violation of subsection (a) shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of Commission**\n**(A) In general**\nThe Federal Trade Commission shall enforce this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(B) Privileges and immunities**\nAny person who violates subsection (a) shall be subject to the penalties, and entitled to the privileges and immunities, provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ). Nothing in this paragraph shall be construed to limit the authority of the Federal Trade Commission under any other provision of law.\n**(3) Regulations**\nThe Federal Trade Commission may promulgate, in accordance with section 553 of title 5, United States Code, such regulations as the Commission considers appropriate to carry out this section.\n##### (c) Enforcement by Attorney General\nThe Attorney General may bring a civil action in the courts of the United States against a person who engages in a violation of subsection (a), for appropriate relief.\n##### (d) Enforcement by States\n**(1) In general**\nIf the attorney general of a State has reason to believe that an interest of the residents of the State has been or is being threatened or adversely affected by a practice that violates subsection (a), the attorney general of the State may, as parens patriae, bring a civil action on behalf of the residents of the State in an appropriate district court of the United States to obtain appropriate relief.\n**(2) Rights of Federal Trade Commission**\n**(A) Notice to Federal Trade Commission**\n**(i) In general**\nExcept as provided in clause (iii), the attorney general of a State, before initiating a civil action under paragraph (1), shall provide written notification to the Federal Trade Commission that the attorney general intends to bring such civil action.\n**(ii) Contents**\nThe notification required under clause (i) shall include a copy of the complaint to be filed to initiate the civil action.\n**(iii) Exception**\nIf it is not feasible for the attorney general of a State to provide the notification required under clause (i) before initiating a civil action under paragraph (1), the attorney general shall notify the Commission immediately upon instituting the civil action.\n**(B) Intervention by Federal Trade Commission**\nThe Commission may\u2014\n**(i)**\nintervene in any civil action brought by the attorney general of a State under paragraph (1); and\n**(ii)**\nupon intervening\u2014\n**(I)**\nbe heard on all matters arising in the civil action; and\n**(II)**\nfile petitions for appeal of a decision in the civil action.\n**(3) Investigatory powers**\nNothing in this subsection may be construed to prevent the attorney general of a State from exercising the powers conferred on the attorney general by the laws of the State to conduct investigations, to administer oaths or affirmations, or to compel the attendance of witnesses or the production of documentary or other evidence.\n**(4) Preemptive action by Federal Trade Commission**\nIf the Federal Trade Commission institutes a civil action or an administrative action with respect to a violation of subsection (a), the attorney general of a State may not, during the pendency of such action, bring a civil action under paragraph (1) against any defendant named in the complaint of the Commission for the violation with respect to which the Commission instituted such action.\n**(5) Venue; service of process**\n**(A) Venue**\nAny action brought under paragraph (1) may be brought in\u2014\n**(i)**\nthe district court of the United States that meets applicable requirements relating to venue under section 1391 of title 28, United States Code; or\n**(ii)**\nanother court of competent jurisdiction.\n**(B) Service of process**\nIn an action brought under paragraph (1), process may be served in any district in which\u2014\n**(i)**\nthe defendant is an inhabitant, may be found, or transacts business; or\n**(ii)**\nvenue is proper under section 1391 of title 28, United States Code.\n**(6) Actions by other State officials**\n**(A) In general**\nIn addition to a civil action brought by an attorney general under paragraph (1), any other officer of a State who is authorized by the State to do so may bring a civil action under paragraph (1), subject to the same requirements and limitations that apply under this subsection to civil actions brought by attorneys general.\n**(B) Savings provision**\nNothing in this subsection may be construed to prohibit an authorized official of a State from initiating or continuing any proceeding in a court of the State for a violation of any civil or criminal law of the State.\n#### 5. Severability\nIf any provision of this Act, or the application of such provision to any person or circumstance, is held to be unconstitutional, the remainder of this Act, and its application to any person or circumstance shall not be affected thereby.",
      "versionDate": "2025-05-07",
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
        "actionDate": "2025-05-07",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "3243",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Therapeutic Fraud Prevention Act of 2025",
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
        "name": "Commerce",
        "updateDate": "2025-06-09T14:42:46Z"
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
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1663is.xml"
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
      "title": "Therapeutic Fraud Prevention Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-28T04:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Therapeutic Fraud Prevention Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T04:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit commercial sexual orientation conversion therapy, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T04:03:33Z"
    }
  ]
}
```
