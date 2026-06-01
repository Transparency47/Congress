# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4227?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4227
- Title: AMMO Act
- Congress: 119
- Bill type: HR
- Bill number: 4227
- Origin chamber: House
- Introduced date: 2025-06-27
- Update date: 2026-02-04T04:26:31Z
- Update date including text: 2026-02-04T04:26:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-27: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-27: Introduced in House

## Actions

- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-27",
    "latestAction": {
      "actionDate": "2025-06-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4227",
    "number": "4227",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000598",
        "district": "42",
        "firstName": "Robert",
        "fullName": "Rep. Garcia, Robert [D-CA-42]",
        "lastName": "Garcia",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "AMMO Act",
    "type": "HR",
    "updateDate": "2026-02-04T04:26:31Z",
    "updateDateIncludingText": "2026-02-04T04:26:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-27",
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
      "actionDate": "2025-06-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-27",
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
          "date": "2025-06-27T13:02:05Z",
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
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "FL"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "FL"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "MA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "MI"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "NM"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "NY"
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
      "sponsorshipDate": "2025-06-27",
      "state": "GA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "IL"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "True",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "CA"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "VT"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "IL"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "IL"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "AL"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "NY"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "NY"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "CA"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "CA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "CA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "RI"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "CA"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "IL"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "IL"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "PA"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "KY"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "TX"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "TX"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "CA"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "NC"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "MA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "CA"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4227ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4227\nIN THE HOUSE OF REPRESENTATIVES\nJune 27, 2025 Mr. Garcia of California (for himself, Ms. Wasserman Schultz , Mr. Frost , Mr. Lynch , Mr. Thanedar , Ms. Stansbury , Mr. Torres of New York , Mr. Johnson of Georgia , Mrs. Ramirez , Mr. Vargas , Ms. Balint , Ms. Schakowsky , Mr. Quigley , Ms. Sewell , Mr. Espaillat , Mr. Goldman of New York , Ms. Brownley , Mr. Swalwell , Mr. Mullin , Mr. Magaziner , Ms. Barrag\u00e1n , Ms. Kelly of Illinois , Mr. Casten , and Mr. Deluzio ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to prevent bulk sales of ammunition, promote recordkeeping and reporting about ammunition, end ammunition straw purchasing, and require a background check before the transfer of ammunition by certain Federal firearms licensees to non-licensees.\n#### 1. Short title\nThis Act may be cited as the Ammunition Modernization and Monitoring Oversight Act or the AMMO Act .\n#### 2. Federal license required to deal in ammunition\n##### (a) In general\nSection 922(a)(1)(B) of title 18, United States Code, is amended\u2014\n**(1)**\nby striking or licensed manufacturer and inserting licensed manufacturer, or licensed dealer ; and\n**(2)**\nby striking or manufacturing and inserting manufacturing, or dealing in .\n##### (b) Conforming amendments\n**(1) Definition of dealer**\nSection 921(a)(11)(A) of such title is amended by inserting or ammunition after firearms .\n**(2) License fee**\nSection 923(a)(3)(B) of such title is amended by striking who is not a dealer in destructive devices and inserting in firearms other than destructive devices or ammunition for firearms other than destructive devices .\n#### 3. Ammunition recordkeeping requirement for certain licensees\nSection 923(g)(1) of title 18, United States Code, is amended\u2014\n**(1)**\nin subparagraph (A), by inserting or ammunition after firearms ; and\n**(2)**\nin each of subparagraphs (B)(iii) and (C)(ii), by inserting , or of ammunition, after firearms .\n#### 4. Prohibition on straw purchase of ammunition\nSection 932 of title 18, United States Code, is amended in each of subsections (b) and (c)(2), by inserting or ammunition after firearm each place it appears.\n#### 5. Restriction on bulk ammunition sales\n##### (a) In general\nSection 922 of title 18, United States Code, is amended by adding at the end the following:\n(aa) (1) It shall be unlawful for any person licensed under this chapter to transfer to a person not so licensed\u2014 (A) more than 100 rounds of .50 caliber ammunition or more than 1,000 rounds of any other caliber of ammunition in any period of 5 consecutive days; or (B) any ammunition if\u2014 (i) the transferee has not provided to the transferor a written certification, signed by the transferee, attesting that the purchase of the ammunition would not result in the transferee having acquired more than 100 rounds of .50 caliber ammunition or more than 1,000 rounds of any other caliber of ammunition, in the 5-day period ending with the date of the transfer; or (ii) the transferor knows or has reason to believe that the transfer would result in the transferee having acquired more than 100 rounds of .50 caliber ammunition or more than 1,000 rounds of any other caliber of ammunition, in the 5-day period ending with the date of the transfer. (2) (A) It shall be unlawful for a person licensed under this chapter to transfer ammunition to a person not so licensed, unless the transferee\u2014 (i) has presented to the licensee a valid identification document (as defined in section 1028(d)) on which appears\u2014 (I) the name and address of the transferee; (II) a number unique to the transferee; and (III) the signature of the transferee; and (ii) has entered the name, address, and signature of the transferee on, and otherwise completed, such form as the Attorney General shall prescribe, which shall include the written certification described in paragraph (1)(B), and a statement of the penalties for violating this subsection. (B) It shall be unlawful for any person in connection with the purchase or attempted purchase of ammunition to knowingly make any false or fictitious oral or written statement or to furnish or exhibit any false, fictitious, or misrepresented identification, intended or likely to deceive the seller with respect to any fact material to the lawfulness of the sale of the ammunition under this chapter. (C) (i) Within 30 calendar days after the date a person licensed under this chapter transfers ammunition in a transaction subject to paragraph (1), the licensee shall transmit to the Attorney General a paper or electronic copy of the form completed by the transferee pursuant to subparagraph (A) of this paragraph. (ii) The Attorney General shall determine, on the basis of the forms transmitted pursuant to clause (i) of this subparagraph, whether a transfer of ammunition has been made in violation of paragraph (1)(A). (iii) Within 60 days after receipt of a form pursuant to clause (i), the Attorney General shall destroy the form unless the form is needed in an ongoing bona fide criminal investigation or prosecution. (D) A licensee who transfers ammunition in a transaction subject to paragraph (1) shall keep the form referred to in subparagraph (C) of this paragraph in paper or electronic form for not fewer than 2 years. .\n##### (b) Penalties\nSection 924(a) of such title is amended by adding at the end the following:\n(9) (A) A person licensed under this chapter who knowingly violates paragraph (1) or (2)(A) of section 922(aa) shall be fined not less than $50,000 and not more than $250,000, and\u2014 (i) in the case of the 2nd such violation by the person, the person shall be prohibited from selling a firearm or ammunition for 60 days; or (ii) in the case of the 3rd such violation by the person, all licenses issued to the person under this chapter shall be revoked. (B) A person who knowingly violates section 922(aa)(2)(B) shall be\u2014 (i) fined not more than\u2014 (I) $20,000, in the case of the 1st such violation by the person; or (II) $50,000, in the case of any subsequent such violation by the person; (ii) imprisoned not more than 5 years; or (iii) both. (C) Whoever knowingly violates subparagraph (C)(i) or (D) of section 922(aa)(2) shall be fined not more than $10,000. .\n##### (c) Signage requirement\n**(1) In general**\nSection 923(g) of such title is amended by adding at the end the following:\n(8) Each person licensed under this chapter shall post at the premises of the licensee subject to the license a sign on which there is set forth, in accordance with regulations prescribed by the Attorney General\u2014 (A) a summary of paragraphs (1) and (2)(B) of section 922(aa), and the penalties for making false statements on a written certification made pursuant to section 922(aa)(1)(B)(i); and (B) a summary of the provisions of section 932 relating to ammunition, and the penalties for violating those provisions. .\n**(2) Penalty**\nSection 924 of such title is amended by adding at the end the following:\n(q) Civil penalty for failure of licensee To post sign about restrictions on ammunition sales (1) In general (A) Civil penalty With respect to each violation of section 923(g)(8) by a person licensed under this chapter, the Attorney General may, after notice and opportunity for hearing, subject the licensee to a civil penalty in an amount equal to $10,000. (B) Review An action under this paragraph may be reviewed only as provided under section 923(f). (2) Administrative remedies The imposition of a civil penalty under paragraph (1) shall not preclude any administrative remedy that is otherwise available to the Attorney General. .\n#### 6. Background check required before transfer of ammunition by certain Federal firearms licensees to non-licensees\n##### (a) In general\nSection 922 of title 18, United States Code, is amended\u2014\n**(1)**\nby striking subsection (s) and redesignating subsection (t) as subsection (s);\n**(2)**\nin subsection (s) (as so redesignated)\u2014\n**(A)**\nin paragraph (1)(B)(i), by inserting indicating that the receipt of a firearm or ammunition by such other person would not violate subsection (g) or (n) of this section, or State, local, or Tribal law before the semicolon;\n**(B)**\nin paragraph (3)(C)(ii), by striking (as defined in subsection (s)(8)) ; and\n**(C)**\nby adding at the end the following:\n(7) In this subsection, the term chief law enforcement officer means the chief of police, the sheriff, or an equivalent officer or the designee of any such individual. ; and\n**(3)**\nby inserting after subsection (s) (as so redesignated) the following:\n(t) (1) A licensed importer, licensed manufacturer, or licensed dealer shall not transfer ammunition to another person not licensed under this chapter, unless\u2014 (A) before the completion of the transfer, the licensee contacts the national instant criminal background check system established under section 103 of the Brady Handgun Violence Prevention Act; (B) the system provides the licensee with a unique identification number indicating that\u2014 (i) the receipt of a firearm or ammunition by such other person would not violate subsection (g) or (n) of this section, or State, local, or Tribal law; and (ii) if such other person has not attained 21 years of age, that a transfer of a firearm or ammunition to such other person would not violate subsection (d) of this section; and (C) the licensee has verified the identity of such other person by examining a valid identification document (as defined in section 1028(d) of this title) of such other person containing a photograph of such other person. (2) Paragraph (1) shall not apply to an ammunition transfer between a licensee and another person if\u2014 (A) such other person has presented to the licensee a permit that\u2014 (i) allows such other person to possess or acquire ammunition, or to possess or acquire a firearm; and (ii) was issued not more than 5 years earlier by the State in which the transfer is to take place; and (B) the law of the State provides that such a permit is to be issued only after an authorized government official has verified that the information available to such official does not indicate that possession of ammunition by such other person would be in violation of law. (3) Paragraphs (2) and (4) through (7) of subsection (s) shall apply with respect to ammunition transfers pursuant to this subsection in the same manner in which such paragraphs apply with respect to firearm transfers. (4) It shall be unlawful for a licensed importer, licensed manufacturer, or licensed dealer to transfer possession of ammunition to another person not so licensed unless the licensee has provided such other person with a notice of the prohibition under paragraph (1), and such other person has certified that such other person has been provided with this notice on a form prescribed by the Attorney General. .\n##### (b) Technical and conforming amendments\n**(1) Section 922**\nSection 922(y)(2) of title 18, United States Code, is amended, in the matter preceding subparagraph (A), by striking , (g)(5)(B), and (s)(3)(B)(v)(II) and inserting and (g)(5)(B) .\n**(2) Consolidated and further continuing appropriations act, 2012**\nSection 511 of title V of division B of the Consolidated and Further Continuing Appropriations Act, 2012 ( 34 U.S.C. 40901 note) is amended by striking subsection 922(t) each place it appears and inserting subsection (s) or (t) of section 922 .\n##### (c) Rules of construction\nNothing in this section, or any amendment made by this section, shall be construed to\u2014\n**(1)**\nauthorize the establishment, directly or indirectly, of a national firearms or ammunition registry; or\n**(2)**\ninterfere with the authority of a State, under section 927 of title 18, United States Code, to enact a law on the same subject matter as this section.\n##### (d) Authorization of increased funding for the NICS system\nIn addition to any amount otherwise authorized to be appropriated for the background check system established under section 103 of the Brady Handgun Violence Prevention Act, there are authorized to be appropriated not more than $150,000,000 for upgrading and maintaining the system.\n#### 7. Reporting requirement\nWithin 6 months after the effective date of this Act and annually thereafter, the Director of the Bureau of Alcohol, Tobacco, Firearms and Explosives shall prepare, publish in the Federal Register, and otherwise make available to the public a report on the violations of section 922(aa) of title 18, United States Code, that occurred during the period covered by the report, and the information reported pursuant to paragraph (2)(C) of such section (including geographic data, total sales data, crime statistics, information on repeat offenders, or caliber types involved) during the period covered by the report, which shall include an identification of any trend in the violations or information that Federal, State, or local law enforcement authorities may find useful.\n#### 8. Effective date\nThis Act and the amendments made by this Act shall take effect on the 120th day after the date of the enactment of this Act.",
      "versionDate": "2025-06-27",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-06-26",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "2191",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "AMMO Act",
      "type": "S"
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
        "updateDate": "2025-07-28T12:50:33Z"
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
      "date": "2025-06-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4227ih.xml"
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
      "title": "AMMO Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:55Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AMMO Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ammunition Modernization and Monitoring Oversight Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to prevent bulk sales of ammunition, promote recordkeeping and reporting about ammunition, end ammunition straw purchasing, and require a background check before the transfer of ammunition by certain Federal firearms licensees to non-licensees.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-16T04:18:26Z"
    }
  ]
}
```
