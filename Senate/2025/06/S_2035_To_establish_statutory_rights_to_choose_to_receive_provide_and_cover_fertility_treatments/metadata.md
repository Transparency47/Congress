# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2035?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2035
- Title: Protect IVF Act
- Congress: 119
- Bill type: S
- Bill number: 2035
- Origin chamber: Senate
- Introduced date: 2025-06-11
- Update date: 2025-12-19T12:03:16Z
- Update date including text: 2025-12-19T12:03:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-11: Introduced in Senate
- 2025-06-11 - IntroReferral: Introduced in Senate
- 2025-06-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-06-11: Introduced in Senate

## Actions

- 2025-06-11 - IntroReferral: Introduced in Senate
- 2025-06-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-11",
    "latestAction": {
      "actionDate": "2025-06-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2035",
    "number": "2035",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000622",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Duckworth, Tammy [D-IL]",
        "lastName": "Duckworth",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Protect IVF Act",
    "type": "S",
    "updateDate": "2025-12-19T12:03:16Z",
    "updateDateIncludingText": "2025-12-19T12:03:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-11",
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
      "actionDate": "2025-06-11",
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
          "date": "2025-06-11T18:43:54Z",
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
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "WA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "NJ"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "NY"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "RI"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "MA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "CA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "VT"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "WA"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "PA"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "CO"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "OR"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "HI"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "VA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "MN"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "MD"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "DE"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-06-11",
      "state": "ME"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "CT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "RI"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-06-11",
      "state": "VT"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "MI"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "AZ"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "IL"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "NM"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "HI"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "NH"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "NV"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "CT"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "NY"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "WI"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "VA"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "GA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "CA"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CO"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2035is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2035\nIN THE SENATE OF THE UNITED STATES\nJune 11, 2025 Ms. Duckworth (for herself, Mrs. Murray , Mr. Booker , Mr. Schumer , Mr. Reed , Ms. Warren , Mr. Padilla , Mr. Welch , Ms. Cantwell , Mr. Fetterman , Mr. Hickenlooper , Mr. Merkley , Mr. Schatz , Mr. Warner , Ms. Klobuchar , Ms. Alsobrooks , Mr. Coons , Mr. King , Mr. Blumenthal , Mr. Whitehouse , Mr. Sanders , Mr. Peters , Mr. Gallego , Mr. Durbin , Mr. Heinrich , Ms. Hirono , Mrs. Shaheen , Ms. Rosen , Mr. Murphy , and Mrs. Gillibrand ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo establish statutory rights to choose to receive, provide, and cover fertility treatments, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect IVF Act .\n#### 2. Purposes\nThe purposes of this Act are as follows:\n**(1)**\nTo permit patients to seek and receive fertility treatment, including assisted reproductive technology services, and to permit health care providers that choose to provide fertility treatment, to provide such services without States enacting harmful or unwarranted limitations or requirements that single out the provision of assisted reproductive services for restrictions that are not consistent with widely accepted and evidence-based medical standards of care, and which do not significantly advance reproductive health or the efficacy and safety of fertility treatment, or make fertility treatment more difficult to access.\n**(2)**\nTo promote the right and ability of a patient residing in any State to choose to receive fertility treatment provided in accordance with widely accepted and evidence-based medical standards of care by a health care provider who chooses to provide such services.\n**(3)**\nTo protect an individual\u2019s right to make decisions, in consultation with the individual's health care provider, about the most appropriate medical care to maximize the chance of becoming pregnant and giving birth to a healthy, living, human child with the help of fertility treatment.\n#### 3. Definitions\nIn this Act:\n**(1) Fertility treatment**\nThe term fertility treatment includes the following:\n**(A)**\nPreservation of human oocytes, sperm, or embryos.\n**(B)**\nArtificial insemination, including intravaginal insemination, intracervical insemination, and intrauterine insemination.\n**(C)**\nAssisted reproductive technology, including in vitro fertilization and other treatments or procedures in which reproductive genetic material, such as oocytes, sperm, and embryos, are handled, when clinically appropriate.\n**(D)**\nGenetic testing of embryos.\n**(E)**\nMedications prescribed or obtained over-the-counter, as indicated for fertility.\n**(F)**\nGamete donation.\n**(G)**\nSuch other information, referrals, treatments, procedures, medications, laboratory testing, technologies, and services relating to fertility as the Secretary of Health and Human Services determines appropriate.\n**(2) Health care provider**\nThe term health care provider means any entity or individual (including any physician, nurse practitioner, physician assistant, pharmacist, health care support personnel, clinical staff, and any other individual, as determined by the Secretary of Health and Human Services) that\u2014\n**(A)**\nis engaged or seeks to engage in the delivery of fertility treatment, including through the provision of evidence-based information, counseling, referrals, or items and services that relate to, aid in, or provide fertility treatment; and\n**(B)**\nif required by State law to be licensed, certified, or otherwise authorized to engage in the delivery of such services\u2014\n**(i)**\nis so licensed, certified, or otherwise authorized; or\n**(ii)**\nwould be so licensed, certified, or otherwise authorized but for the fact that the individual or entity has provided, is providing, or plans to provide fertility treatment in accordance with section 4.\n**(3) Health insurance issuer**\nThe term health insurance issuer has the meaning given such term in section 2791(b) of the Public Health Service Act ( 42 U.S.C. 300gg\u201391(b) ).\n**(4) Manufacturer**\nThe term manufacturer means the manufacturer of a drug or device approved, cleared, authorized, or licensed under section 505, 510(k), 513(f)(2), or 515 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 , 360(k), 360c(f)(2), 360e) or section 351 of the Public Health Service Act ( 42 U.S.C. 262 ) or otherwise legally marketed.\n**(5) State**\nThe term State includes each of the 50 States, the District of Columbia, Puerto Rico, each territory and possession of the United States, and any political subdivision thereof.\n**(6) Widely accepted and evidence-based medical standards of care**\nThe term widely accepted and evidence-based medical standards of care means any medical services, procedures, and practices that are in accordance with the guidelines of the American Society for Reproductive Medicine.\n#### 4. Fertility treatment rights\n##### (a) General rule\n**(1) Individual rights**\nAn individual has a statutory right under this Act, without prohibition, limitation, interference, or impediment, to the extent that such prohibition, limitation, interference, or impediment in any way or degree obstructs, delays, or affects commerce over which the Federal Government has jurisdiction, to\u2014\n**(A)**\nreceive fertility treatment from a health care provider, in accordance with widely accepted and evidence-based medical standards of care;\n**(B)**\ncontinue or complete an ongoing fertility treatment previously initiated by a health care provider, in accordance with widely accepted and evidence-based medical standards of care;\n**(C)**\nmake decisions and arrangements regarding the donation, testing, use, storage, or disposition of their own reproductive genetic material; and\n**(D)**\nestablish contractual agreements with a health care provider relating to the health care provider\u2019s services in handling, testing, storing, shipping, and disposing of the individual\u2019s reproductive genetic material in accordance with widely accepted and evidence-based medical standards of care.\n**(2) Health care provider rights**\nA health care provider has a statutory right under this Act, without prohibition, limitation, interference, or impediment, to the extent that such prohibition, limitation, interference, or impediment in any way or degree obstructs, delays, or affects commerce over which the Federal Government has jurisdiction, to\u2014\n**(A)**\nchoose to provide, or assist with the provision of, fertility treatment provided in accordance with widely accepted and evidence-based medical standards of care;\n**(B)**\ncontinue or complete the provision of, or assistance with, fertility treatment that was lawful when commenced and is provided in accordance with widely accepted and evidence-based medical standards of care;\n**(C)**\nprovide for, or assist with, the testing, use, storage, or disposition of reproductive genetic material in accordance with widely accepted and evidence-based medical standards of care; and\n**(D)**\nestablish contractual agreements with individuals or manufacturers relating to the health care provider\u2019s services in handling, testing, storing, shipping, and disposing of the individual\u2019s reproductive genetic material.\n**(3) Health insurance issuer rights**\nA health insurance issuer has a statutory right under this Act, without prohibition, limitation, interference, or impediment, to the extent that such prohibition, limitation, interference, or impediment in any way or degree obstructs, delays, or affects commerce over which the Federal Government has jurisdiction, to choose to cover the provision of fertility treatment provided in accordance with widely accepted and evidence-based medical standards of care.\n**(4) Manufacturer rights**\nA manufacturer of a drug or device that is approved, cleared, authorized, or licensed under section 505, 510(k), 513(f)(2), or 515 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ; 360(k); 360c(f)(2); 360e) or section 351 of the Public Health Service Act ( 42 U.S.C. 262 ) or otherwise legally marketed and intended for use in the provision of fertility treatment, including the storage or transport of reproductive genetic material, has a statutory right under this Act, without prohibition, limitation, interference, or impediment, to the extent that such prohibition, limitation, interference, or impediment in any way or degree obstructs, delays, or affects commerce over which the Federal Government has jurisdiction, to manufacture, import, market, sell, and distribute such drug or device.\n##### (b) State regulation of medicine\nThe enforcement of State health and safety law regarding medical facilities or health care providers does not constitute a violation of subsection (a) if\u2014\n**(1)**\nsuch regulations are in accordance with widely accepted and evidence-based medical standards of care for providing fertility treatment; and\n**(2)**\nthe safety or health objective cannot be advanced by a different means that does not prohibit, limit, interfere with, or impede the rights described in subsection (a).\n##### (c) Enforcement\n**(1) The Attorney General**\n**(A) In general**\nThe Attorney General may commence a civil action on behalf of the United States against any State; an individual, employee, official, agency head, contractor, organization, or instrumentality acting for, or on behalf of, such a State; or any individual acting under the color of, or pursuant to, State law, that implements, enforces, or threatens to enforce a limitation or requirement that prohibits, limits, interferes with, or impedes the statutory rights of an individual, a health care provider, a health insurance issuer, or a manufacturer under subsection (a).\n**(B) Effect of violations**\nThe court shall hold unlawful and set aside a limitation or requirement described in subparagraph (A) if it is in violation of subsection (a).\n**(2) Private right of action**\n**(A) In general**\nAny individual or entity adversely affected by an alleged violation of subsection (a) may commence a civil action against an individual, employee, official, agency head, contractor, organization, or instrumentality acting for, or on behalf of, such a State that enacts, implements, or enforces a limitation or requirement that prohibits, limits, interferes with, or impedes the statutory rights of an individual, a health care provider, a health insurance issuer, or a manufacturer under subsection (a).\n**(B) Effect of violations**\nThe court shall hold unlawful and enjoin a limitation or requirement described in subparagraph (A) if it is in violation of subsection (a).\n**(3) Health care provider**\n**(A) In general**\nA health care provider may commence a civil action for relief on such provider\u2019s own behalf, on behalf of the provider\u2019s staff, or on behalf of the provider\u2019s patients who are or may be adversely affected by an alleged violation of subsection (a).\n**(B) Effect of violations**\nThe court shall hold unlawful and enjoin a limitation or requirement described in subparagraph (A) if it is in violation of subsection (a).\n**(4) Equitable relief**\nIn any action under this section, the court may award appropriate equitable relief, including temporary, preliminary, or permanent injunctive relief.\n**(5) Costs**\n**(A) In general**\nIn any action under this section, the court shall award costs of litigation, as well as reasonable attorney\u2019s fees, to any prevailing plaintiff.\n**(B) Liability of plaintiffs**\nA plaintiff shall not be liable to a defendant for costs or attorney\u2019s fees in any non-frivolous action under this section unless such costs or attorney\u2019s fees are imposed by the court as part of sanctions for violations committed during the discovery process.\n**(6) Jurisdiction**\nThe district courts of the United States shall have jurisdiction over proceedings under this section and shall exercise the same without regard to whether the party aggrieved shall have exhausted any administrative or other remedies that may be provided for by law.\n**(7) Right to remove**\n**(A) In general**\nAny party shall have a right to remove an action brought under this subsection to the district court of the United States for the district and division embracing the place where such action is pending.\n**(B) Review**\nAn order remanding the case to the State court from which it was removed under this paragraph is immediately reviewable by appeal or otherwise.\n##### (d) Rules of construction\n**(1) In general**\nFor purposes of this Act, a State law, or the administration, implementation, or enforcement of a State law, constitutes a prohibition, limitation, interference, or impediment on a health care provider choosing to provide, an individual choosing to receive, a health insurance issuer choosing to cover, or a manufacturer choosing to market drugs or devices for fertility treatment, provided in accordance with widely accepted and evidence-based medical standards of care, as described in section 4, if the administration, implementation, interpretation, or enforcement of such law has an effect that\u2014\n**(A)**\nimposes requirements or limitations that are inconsistent with providing, receiving, providing health insurance coverage for, or providing drugs or devices for fertility treatment in accordance with widely accepted and evidence-based medical standards of care or that otherwise violate the purpose and requirements of this Act, which may include\u2014\n**(i)**\nrequiring that a health care provider provide, and patients undertake, medically unnecessary procedures and services, including tests and procedures, providing medically inaccurate information regarding fertility treatment, or requiring additional unnecessary in-person visits to a health care provider, that are inconsistent with widely accepted and evidence-based medical standards of care;\n**(ii)**\nimposing limitations or requirements concerning physical offices, clinics, facilities, equipment, staffing, or hospital transfer arrangements of facilities where fertility treatment is provided, or the credentials or hospital privileges or status of personnel at such facilities, that are not consistent with widely accepted and evidence-based medical standards of care; or\n**(iii)**\nlimiting a health care provider's right or ability to choose to provide, or a patient\u2019s right to choose to receive, or imposing limitations that reduce the efficacy of, fertility treatment in accordance with widely accepted and evidence-based medical standards of care, including retrieval of multiple eggs during oocyte retrieval; performance of insemination procedures, including intrauterine insemination; intracytoplasmic sperm injections to fertilize multiple human eggs; and cryopreservation of one or more eggs or embryos for fertility preservation, if determined appropriate by the health care provider and patient;\n**(B)**\ninfringes, limits, or restricts the ability of a health care provider, patient, health insurance issuer, or manufacturer, to exercise or enforce their statutory rights under this Act on the basis of marital status, sex (including sexual orientation and gender identity) or any other protected class that is covered by Federal law;\n**(C)**\nlimits a health care provider\u2019s or patient\u2019s right or ability to determine the most appropriate disposition of reproductive genetic materials, including by defining reproductive genetic materials in such a way as to prevent or restrict options for the health care provider or patient;\n**(D)**\nlimits a health care provider\u2019s ability to provide, or a patient\u2019s ability to receive, fertility treatment via telemedicine, in accordance with widely accepted and evidence-based medical standards of care;\n**(E)**\nlimits or prohibits a health care provider\u2019s ability to provide, or a patient\u2019s ability to receive, fertility counseling or fertility treatment based on the residency of the patient, or prohibits or limits the ability of any individual to assist or support a patient seeking fertility treatment;\n**(F)**\nimposes requirements or limitations that compel health care providers to provide, or patients to receive, medically unnecessary care, or withhold medically necessary care, in a manner that is not consistent with widely accepted and evidence-based medical standards of care for fertility treatment, including mandating the transfer of embryos that a health care provider would not reasonably expect, based on widely accepted and evidence-based medical standards of care, to lead to a healthy pregnancy or a live birth;\n**(G)**\nlimits a health care provider\u2019s right or ability to prescribe or dispense, or a patient\u2019s right or ability to receive or use, medications for fertility treatment in accordance with widely accepted and evidence-based medical standards of care, unless such a limitation is generally applicable to the prescription, dispensing, or distribution of medications; or\n**(H)**\nlimits a health care provider\u2019s right or ability to perform a human sperm retrieval procedure in accordance with widely accepted and evidence-based medical standards of care.\n**(2) Clarification**\nThe descriptions of specific State laws that would violate the statutory rights and protections described in paragraph (1) shall not be construed to limit potential violations of the statutory rights and protections under this Act to only the restrictions and limitations listed in paragraph (1), and potential violations of this Act may result from novel State restrictions and limitations that are not listed under paragraph (1).\n**(3) Exclusion**\nIt shall not constitute a prohibition, limitation, interference, or impediment to a health care provider providing, an individual receiving, a health insurance issuer covering, or a manufacturer marketing a drug or device for purposes of, fertility treatment under this Act for an entity to act in compliance with the Food and Drug Administration\u2019s regulation of drugs, devices, biological products, human cells, tissues, or cellular or tissue-based products used in fertility treatment, consistent with widely accepted and evidence-based medical standards of care for fertility treatment.\n#### 5. Applicability and preemption\n##### (a) In general\n**(1) General application**\n**(A) Effect on State law**\nThis Act supersedes any State law that is inconsistent with the statutory rights established under this Act and precludes the implementation of such a law, whether statutory, common law, or otherwise, and whether adopted before or after the date of enactment of this Act.\n**(B) Prohibition**\nNo State shall administer, implement, or enforce any law, rule, regulation, standard, or other provision having the force and effect of law that conflicts with any provision of this Act, notwithstanding any other provision of Federal law.\n**(2) Exclusion**\nPreemption of State law under paragraph (1) does not apply to\u2014\n**(A)**\nState law regarding the resolution of disputes between 2 individuals with rights described in section 4(a)(1) with respect to the same reproductive genetic material; or\n**(B)**\nany other State law, to the extent that such law does not conflict with this Act and protects an individual\u2019s right and ability to receive fertility treatment in accordance with widely accepted and evidence-based medical standards of care, including any such law that holds a health care provider accountable for not providing fertility treatment in accordance with widely accepted and evidence-based medical standards of care.\n**(3) Preservation of Federal public health authorities**\nNothing in this Act shall have the effect of superseding, negating, or limiting provisions of Federal law, including the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 et seq. ) or the Public Health Service Act ( 42 U.S.C. 201 et seq. ), and regulations promulgated under such statutes, with respect to the regulation of drugs, devices, biological products, human cells, tissues, or cellular or tissue-based products used in fertility treatment.\n**(4) Preservation of HIPAA rules**\nNothing in this Act shall have the effect of superseding, negating, or limiting the provisions of the privacy, security, and breach notification regulations in parts 160 and 164 of title 45, Code of Federal Regulations (or successor regulations).\n**(5) Subsequently enacted Federal legislation**\nFederal statutory law adopted after the date of the enactment of this Act is subject to this Act unless such law explicitly excludes such application by reference to this Act.\n##### (b) Defense\nIn any cause of action against an individual or entity who is subject to a limitation or requirement that violates this Act, in addition to the remedies specified in section 4(c), this Act shall also apply to, and may be raised as a defense by, such an individual or entity.",
      "versionDate": "2025-06-11",
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
        "name": "Health",
        "updateDate": "2025-07-03T13:45:56Z"
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
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2035is.xml"
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
      "title": "Protect IVF Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protect IVF Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-21T02:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish statutory rights to choose to receive, provide, and cover fertility treatments, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-21T02:48:40Z"
    }
  ]
}
```
