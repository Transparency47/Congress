# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2180?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/2180
- Title: Global Respect Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2180
- Origin chamber: Senate
- Introduced date: 2025-06-26
- Update date: 2025-07-30T12:48:20Z
- Update date including text: 2025-07-30T12:48:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-26: Introduced in Senate
- 2025-06-26 - IntroReferral: Introduced in Senate
- 2025-06-26 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-06-26: Introduced in Senate

## Actions

- 2025-06-26 - IntroReferral: Introduced in Senate
- 2025-06-26 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/2180",
    "number": "2180",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Global Respect Act of 2025",
    "type": "S",
    "updateDate": "2025-07-30T12:48:20Z",
    "updateDateIncludingText": "2025-07-30T12:48:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-26",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T20:04:51Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "AK"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "CT"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "MD"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "OR"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "NJ"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "VT"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "MA"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "HI"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "WI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "OR"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NV"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MN"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2180is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2180\nIN THE SENATE OF THE UNITED STATES\nJune 26 (legislative day, June 24), 2025 Mrs. Shaheen (for herself, Ms. Murkowski , Mr. Murphy , Mr. Van Hollen , Mr. Merkley , Mr. Booker , Mr. Welch , Mr. Markey , Mr. Schatz , Ms. Baldwin , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo impose sanctions with respect to foreign persons responsible for violations of the human rights of lesbian, gay, bisexual, transgender, queer, and intersex (LGBTQI) individuals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Global Respect Act of 2025 .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nThe dignity, freedom, and equality of all human beings are fundamental to a thriving global community.\n**(2)**\nThe rights to life, liberty, and security of the person, the right to privacy, and the right to freedom of expression and association are fundamental human rights.\n**(3)**\nMany countries have made and are making positive developments in the protection of the basic human rights of LGBQTI individuals.\n**(4)**\nThe alarming trend of increasing violence directed at lesbian, gay, bisexual, transgender, queer, and intersex (commonly referred to as LGBTQI ) individuals around the world continues.\n**(5)**\nApproximately 1/3 of all countries have laws criminalizing consensual same-sex relations, and 12 countries carry the possibility of the death penalty.\n**(6)**\nLaws criminalizing consensual same-sex relations severely hinder access to HIV/AIDS treatment, information, and prevention measures for LGBTQI individuals and families.\n**(7)**\nCelebrations of LGBTQI individuals and communities, such as film festivals, Pride events, and demonstrations, are often forced underground due to inaction on the part of, or harassment by, local law enforcement and government officials, in violation of freedoms of assembly and expression.\n**(8)**\nEvery year, countless individuals around the world are targeted for discrimination, harassment, arbitrary arrest and detention, physical attack, and murder on the basis of their actual or perceived sexual orientation, gender identity, or sex characteristics.\n**(9)**\nThose who commit crimes against LGBTQI individuals often do so with impunity, and are not held accountable for their crimes.\n**(10)**\nHomophobic and transphobic statements by government officials in many countries in every region of the world promote negative public attitudes and can lead to increased discrimination and violence toward LGBTQI individuals.\n**(11)**\nIn many instances, police, prison, military, and civilian government authorities have been directly complicit in abuses aimed at LGBTQI citizens, including arbitrary arrest, extortion, cruel, inhuman, or degrading treatment, torture, and sexual abuse.\n#### 3. Definitions\nIn this Act:\n**(1) Admission; admitted**\nThe terms admission and admitted have the meanings given those terms in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 ).\n**(2) Appropriate congressional committees**\nThe term appropriate congressional committees means the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives.\n**(3) Foreign person**\nThe term foreign person means\u2014\n**(A)**\nan individual who is a citizen or national of a foreign country (including any such individual who is also a citizen or national of the United States), including leaders or officials of governmental entities of a foreign country; or\n**(B)**\nany entity not organized solely under the laws of the United States or existing solely in the United States, including governmental entities of a foreign country.\n#### 4. Identification of foreign persons responsible for violations of human rights of LGBTQI individuals\n##### (a) List required\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, and every 180 days thereafter, the President shall submit to the appropriate congressional committees a list of each foreign person that the President determines, based on credible information, on or after such date of enactment\u2014\n**(A)**\nengages in, is responsible for, or is complicit in, conduct described in paragraph (2);\n**(B)**\nacts as an agent of or on behalf of a foreign person in a matter relating to conduct described in paragraph (2); or\n**(C)**\nis responsible for, or complicit in, inciting a foreign person to engage in conduct described in paragraph (2).\n**(2) Conduct described**\nConduct described in this paragraph is any of the following, conducted with respect to an individual based on the actual or perceived sexual orientation, gender identity, or sex characteristics of the individual:\n**(A)**\nTorture or cruel, inhuman, or degrading treatment or punishment of the individual.\n**(B)**\nProlonged detention of the individual without charges or trial.\n**(C)**\nCausing the disappearance of the individual by the abduction and clandestine detention of the individual.\n**(D)**\nOther flagrant denial of the right to life, liberty, or the security of the individual.\n**(3) Credible information**\nFor purposes of paragraph (1), credible information includes information obtained by other countries or nongovernmental organizations that monitor violations of human rights.\n##### (b) Updates\nThe President shall submit to the appropriate congressional committees an update of the list required by subsection (a) as new information becomes available.\n##### (c) Removal\nA person may be removed from the list required by subsection (a) if the President determines and reports to the appropriate congressional committees not later than 15 days before the removal of the person from the list that\u2014\n**(1)**\ncredible information exists that the person did not engage in the activity for which the person was added to the list;\n**(2)**\nthe person has been prosecuted appropriately for the activity; or\n**(3)**\nthe person has credibly demonstrated a significant change in behavior, has paid an appropriate consequence for the activity, and has credibly committed to not engage in an activity described in subsection (a) in the future.\n##### (d) Form\n**(1) In general**\nThe list required by subsection (a)\u2014\n**(A)**\nshall, notwithstanding the requirements of section 222(f) of the Immigration and Nationality Act ( 8 U.S.C. 1202(f) ) with respect to confidentiality of records pertaining to the issuance or refusal of visas or permits to enter the United States, be submitted in unclassified form and be published in the Federal Register; and\n**(B)**\nmay include a classified annex only as provided in paragraph (2).\n**(2) Use of classified annex**\nThe President may include a person on the list required by subsection (a) in a classified annex to the list if the President\u2014\n**(A)**\ndetermines that\u2014\n**(i)**\nit is vital for the national security interests of the United States to do so; and\n**(ii)**\nthe use of the annex, and the inclusion of the person in the annex, would not undermine the overall purpose of this section to publicly identify foreign persons engaging in activities described in subsection (a) in order to increase accountability for such conduct; and\n**(B)**\nnot later than 15 days before including the person in the annex, submits to the appropriate congressional committees notice of, and a justification for, including or continuing to include the person in the classified annex despite the existence of any publicly available credible information indicating that the person engaged in an activity described in subsection (a).\n##### (e) Public submission of information\nThe President shall issue public guidance, including through United States diplomatic and consular posts, setting forth the manner by which the names of foreign persons that may meet the criteria to be included on the list required by subsection (a) may be submitted to the Secretary of State for evaluation.\n##### (f) Requests from appropriate congressional committees\n**(1) Consideration of information**\nThe President shall consider information provided by the chairperson or ranking member of any of the appropriate congressional committees in determining whether to include a foreign person on the list required by subsection (a).\n**(2) Requests**\nNot later than 120 days after receiving a written request from the chairperson or ranking member of one of the appropriate congressional committees with respect to whether a foreign person meets the criteria for being added to the list required by subsection (a), the President shall submit a response to the chairperson or ranking member, as the case may be, with respect to the determination of the President with respect to the person.\n**(3) Removal**\nIf the President removes from the list required by subsection (a) a person that had been placed on the list pursuant to a request the chairperson or ranking member of one of the appropriate congressional committees under paragraph (2), the President shall provide to the chairperson or ranking member any information that contributed to the decision to remove the person from the list.\n**(4) Form**\nThe President may submit a response required by paragraph (2) or (3) in classified form if the President determines that it is necessary for the national security interests of the United States to do so.\n#### 5. Inadmissibility of individuals responsible for violations of human rights of LGBTQI individuals\n##### (a) Ineligibility for visas and admission to the United States\nAn individual who is a foreign person on the list required by section 4(a) is ineligible to receive a visa to enter the United States and ineligible to be admitted to the United States.\n##### (b) Current visas revoked and removal from United States\n**(1) In general**\nThe Secretary of State shall revoke, in accordance with section 221(i) of the Immigration and Nationality Act ( 8 U.S.C. 1201(i) ), the visa or other documentation of an individual on the list required by section 4(a), and the Secretary of Homeland Security shall remove any such individual from the United States.\n**(2) Regulations required**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State and the Secretary of Homeland Security shall prescribe such regulations as are necessary to carry out this subsection.\n##### (c) Waivers\nThe President may waive the application of subsection (a) or (b) with respect to a foreign person if the President\u2014\n**(1)**\ndetermines that such a waiver\u2014\n**(A)**\nis necessary to permit the United States to comply with the Agreement regarding the Headquarters of the United Nations, signed at Lake Success June 26, 1947, and entered into force November 21, 1947, between the United Nations and the United States, the Convention on Consular Relations, done at Vienna April 24, 1963, and entered into force March 19, 1967, or other applicable international obligations of the United States; or\n**(B)**\nis in the national security interests of the United States; and\n**(2)**\nnot less than 15 days before the granting of the waiver, submits to the appropriate congressional committees a notice of and justification for the waiver.\n#### 6. Sense of Congress with respect to additional sanctions\nIt is the sense of Congress that the President should use existing authorities to impose targeted sanctions (in addition to section 5) with respect to foreign persons on the list required by section 4(a) to push for accountability for flagrant denials of the right to life, liberty, or the security of the person.\n#### 7. Report to Congress\nNot later than one year after the date of the enactment of this Act, and annually thereafter, the Secretary of State shall submit to the appropriate congressional committees a report on\u2014\n**(1)**\nthe actions taken to carry out this Act, including\u2014\n**(A)**\nthe number of foreign persons added to or removed from the list required by section 4(a) during the year preceding the report, the dates on which those persons were added or removed, and the reasons for adding or removing those persons; and\n**(B)**\nin each report after the first such report, an analysis that compares increases or decreases in the number of persons added to or removed from the list year-over-year and the reasons for such increases or decreases; and\n**(2)**\nany efforts by the President to coordinate with the governments of other countries, as appropriate, to impose sanctions that are similar to the sanctions imposed under this Act.\n#### 8. Discrimination related to sexual orientation or gender identity\n##### (a) Tracking violence or criminalization related to sexual orientation or gender identity\nThe Assistant Secretary of State for Democracy, Human Rights, and Labor shall designate a Bureau-based senior officer or officers who shall be responsible for tracking violence, criminalization, and restrictions on the enjoyment of fundamental freedoms in foreign countries based on actual or perceived sexual orientation, gender identity, or sex characteristics.\n##### (b) Annual country reports on human rights practices\nThe Foreign Assistance Act of 1961 is amended\u2014\n**(1)**\nin section 116(d) ( 22 U.S.C. 2151n(d) )\u2014\n**(A)**\nin paragraph (12)(C), by striking the period at the end and inserting a semicolon;\n**(B)**\nin paragraph (13)\u2014\n**(i)**\nby striking Wherever and inserting wherever ; and\n**(ii)**\nin subparagraph (E), by striking the period at the end and inserting and ; and\n**(C)**\nby adding at the end the following new paragraph:\n(14) wherever applicable, violence or discrimination that affects the fundamental freedoms, including widespread or systematic violation of the freedoms of expression, association, or assembly of an individual in foreign countries that is based on actual or perceived sexual orientation, gender identity, or sex characteristics. ; and\n**(2)**\nin section 502B(b) ( 22 U.S.C. 2304(b) ), by inserting after the ninth sentence the following: Wherever applicable, each report under this section shall also include information regarding violence or discrimination that affects the fundamental freedoms, including widespread or systematic violation of the freedoms of expression, association, or assembly of an individual in foreign countries that is based on actual or perceived sexual orientation, gender identity, or sex characteristics. .",
      "versionDate": "2025-06-26",
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
        "name": "International Affairs",
        "updateDate": "2025-07-17T21:37:07Z"
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
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2180is.xml"
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
      "title": "Global Respect Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:48:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Global Respect Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-15T17:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to impose sanctions with respect to foreign persons responsible for violations of the human rights of lesbian, gay, bisexual, transgender, queer, and intersex (LGBTQI) individuals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-15T17:18:28Z"
    }
  ]
}
```
