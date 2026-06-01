# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2191?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2191
- Title: AMMO Act
- Congress: 119
- Bill type: S
- Bill number: 2191
- Origin chamber: Senate
- Introduced date: 2025-06-26
- Update date: 2025-10-09T11:03:14Z
- Update date including text: 2025-10-09T11:03:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-26: Introduced in Senate
- 2025-06-26 - IntroReferral: Introduced in Senate
- 2025-06-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-06-26: Introduced in Senate

## Actions

- 2025-06-26 - IntroReferral: Introduced in Senate
- 2025-06-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2191",
    "number": "2191",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "W000817",
        "district": "",
        "firstName": "Elizabeth",
        "fullName": "Sen. Warren, Elizabeth [D-MA]",
        "lastName": "Warren",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "AMMO Act",
    "type": "S",
    "updateDate": "2025-10-09T11:03:14Z",
    "updateDateIncludingText": "2025-10-09T11:03:14Z"
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
          "date": "2025-06-26T20:46:57Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "CT"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "HI"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2191is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2191\nIN THE SENATE OF THE UNITED STATES\nJune 26 (legislative day, June 24), 2025 Ms. Warren (for herself, Mr. Blumenthal , and Ms. Hirono ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to prevent bulk sales of ammunition, promote recordkeeping and reporting about ammunition, end ammunition straw purchasing, and require a background check before the transfer of ammunition by certain Federal firearms licensees to non-licensees.\n#### 1. Short title\nThis Act may be cited as the Ammunition Modernization and Monitoring Oversight Act or the AMMO Act .\n#### 2. Federal license required to deal in ammunition\n##### (a) In general\nSection 922(a)(1)(B) of title 18, United States Code, is amended\u2014\n**(1)**\nby striking or licensed manufacturer and inserting , licensed manufacturer, or licensed dealer ; and\n**(2)**\nby striking or manufacturing and inserting , manufacturing, or dealing in .\n##### (b) Conforming amendments\n**(1) Definition of dealer**\nSection 921(a)(11)(A) of title 18, United States Code, is amended by inserting or ammunition after firearms .\n**(2) License fee**\nSection 923(a)(3)(B) of title 18, United States Code, is amended by striking who is not a dealer in destructive devices and inserting in firearms other than destructive devices or ammunition for firearms other than destructive devices .\n#### 3. Ammunition recordkeeping requirement for certain licensees\nSection 923(g)(1) of title 18, United States Code, is amended\u2014\n**(1)**\nin subparagraph (A), in the first sentence, by inserting or ammunition after firearms ;\n**(2)**\nin subparagraph (B)(iii), by inserting , or of ammunition, after firearms ; and\n**(3)**\nin subparagraph (C)(ii), by inserting , or of ammunition, after firearms .\n#### 4. Prohibition on straw purchase of ammunition\nSection 932 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (b), by inserting or ammunition after firearm each place it appears; and\n**(2)**\nin subsection (c)(2), by inserting or ammunition after firearm .\n#### 5. Restriction on bulk ammunition sales\n##### (a) In general\nSection 922 of title 18, United States Code, is amended by adding at the end the following:\n(aa) Restriction on bulk ammunition sales (1) In general It shall be unlawful for any person licensed under this chapter to transfer to a person not so licensed\u2014 (A) during any 5-day period\u2014 (i) more than 100 rounds of .50 caliber ammunition; or (ii) more than 1,000 rounds of any other caliber of ammunition; or (B) any ammunition if\u2014 (i) the transferee has not provided to the transferor a written certification, signed by the transferee, attesting that the purchase of the ammunition would not result in the transferee having acquired, during the 5-day period ending on the date of the transfer\u2014 (I) more than 100 rounds of .50 caliber ammunition; or (II) more than 1,000 rounds of any other caliber of ammunition; or (ii) the transferor knows or has reason to believe that the transfer would result in the transferee having acquired, during the 5-day period ending on the date of the transfer\u2014 (I) more than 100 rounds of .50 caliber ammunition; or (II) more than 1,000 rounds of any other caliber of ammunition. (2) Administrative requirements (A) Identification document; Attorney General form It shall be unlawful for a person licensed under this chapter to transfer ammunition to a person not so licensed, unless the transferee\u2014 (i) has presented to the licensee a valid identification document (as defined in section 1028(d)) on which appears\u2014 (I) the name and address of the transferee; (II) a number unique to the transferee; and (III) the signature of the transferee; and (ii) has entered the name, address, and signature of the transferee on, and otherwise completed, such form as the Attorney General shall prescribe, which shall include\u2014 (I) the written certification described in paragraph (1)(B)(i); and (II) a statement of the penalties for violating this subsection. (B) False statement or identification It shall be unlawful for any person in connection with the purchase or attempted purchase of ammunition to knowingly make any false or fictitious oral or written statement or to furnish or exhibit any false, fictitious, or misrepresented identification, intended or likely to deceive the seller with respect to any fact material to the lawfulness of the sale of the ammunition under this chapter. (C) Transmission of form to Attorney General (i) In general Not later than 30 days after the date on which a person licensed under this chapter transfers ammunition in a transaction subject to paragraph (1), the licensee shall transmit to the Attorney General a paper or electronic copy of the form completed by the transferee pursuant to subparagraph (A) of this paragraph. (ii) Determination of violation The Attorney General shall determine, on the basis of the forms transmitted pursuant to clause (i) of this subparagraph, whether a transfer of ammunition has been made in violation of paragraph (1)(A). (iii) Destruction of form Not later than 60 days after receipt of a form pursuant to clause (i), the Attorney General shall destroy the form unless the form is needed in an ongoing bona fide criminal investigation or prosecution. (D) Recordkeeping requirement A licensee who transfers ammunition in a transaction subject to paragraph (1) shall keep the form referred to in subparagraph (C) of this paragraph in paper or electronic form for not fewer than 2 years. .\n##### (b) Penalties\nSection 924(a) of title 18, United States Code, is amended by adding at the end the following:\n(9) (A) If a person licensed under this chapter knowingly violates paragraph (1) or (2)(A) of section 922(aa)\u2014 (i) in the case of the first violation, the person shall be fined not less than $50,000 and not more than $250,000; (ii) in the case of the second violation, the person shall be prohibited from selling a firearm or ammunition for 60 days; or (iii) in the case of the third violation, all licenses issued to the person under this chapter shall be revoked. (B) A person who knowingly violates section 922(aa)(2)(B) shall be\u2014 (i) fined not more than\u2014 (I) $20,000, in the case of the first violation; or (II) $50,000, in the case of any subsequent violation; (ii) imprisoned not more than 5 years; or (iii) both. (C) A person who knowingly violates subparagraph (C)(i) or (D) of section 922(aa)(2) shall be fined not more than $10,000. .\n##### (c) Signage requirement\n**(1) In general**\nSection 923(g) of title 18, United States Code, is amended by adding at the end the following:\n(8) Each person licensed under this chapter shall post at the premises of the licensee subject to the license a sign on which there is set forth, in accordance with regulations prescribed by the Attorney General\u2014 (A) a summary of paragraphs (1) and (2)(B) of section 922(aa), and the penalties for making false statements on a written certification made pursuant to section 922(aa)(1)(B)(i); and (B) a summary of the provisions of section 932 relating to ammunition, and the penalties for violating those provisions. .\n**(2) Penalty**\nSection 924 of title 18, United States Code, is amended by adding at the end the following:\n(q) Civil penalty for failure of licensee To post sign about restrictions on ammunition sales (1) In general (A) Civil penalty With respect to each violation of section 923(g)(8) by a person licensed under this chapter, the Attorney General may, after notice and opportunity for hearing, subject the licensee to a civil penalty in an amount equal to $10,000. (B) Review The imposition of a civil penalty under subparagraph (A) may be reviewed only as provided under section 923(f). (2) Administrative remedies The imposition of a civil penalty under paragraph (1) shall not preclude any administrative remedy that is otherwise available to the Attorney General. .\n#### 6. Background check required before transfer of ammunition by certain Federal firearms licensees to non-licensees\n##### (a) In general\nSection 922 of title 18, United States Code, is amended\u2014\n**(1)**\nby striking subsection (s) and redesignating subsection (t) as subsection (s);\n**(2)**\nin subsection (s) (as so redesignated)\u2014\n**(A)**\nin paragraph (1)(B)(i), by inserting indicating that the receipt of a firearm or ammunition by such other person would not violate subsection (g) or (n) of this section, or State, local, or Tribal law before the semicolon;\n**(B)**\nin paragraph (3)(C)(ii), by striking (as defined in subsection (s)(8)) ; and\n**(C)**\nby adding at the end the following:\n(7) In this subsection, the term chief law enforcement officer means the chief of police, the sheriff, or an equivalent officer or the designee of any such individual. ; and\n**(3)**\nby inserting after subsection (s) (as so redesignated) the following:\n(t) (1) A licensed importer, licensed manufacturer, or licensed dealer shall not transfer ammunition to another person not licensed under this chapter, unless\u2014 (A) before the completion of the transfer, the licensee contacts the national instant criminal background check system established under section 103 of the Brady Handgun Violence Prevention Act ( 34 U.S.C. 40901 ); (B) the system provides the licensee with a unique identification number indicating\u2014 (i) that the receipt of a firearm or ammunition by such other person would not violate subsection (g) or (n) of this section, or State, local, or Tribal law; and (ii) if such other person has not attained 21 years of age, that a transfer of a firearm or ammunition to such other person would not violate subsection (d) of this section; and (C) the licensee has verified the identity of such other person by examining a valid identification document (as defined in section 1028(d) of this title) of such other person containing a photograph of such other person. (2) Paragraph (1) shall not apply to an ammunition transfer between a licensee and another person if\u2014 (A) such other person has presented to the licensee a permit that\u2014 (i) allows such other person to possess or acquire ammunition, or to possess or acquire a firearm; and (ii) was issued not more than 5 years earlier by the State in which the transfer is to take place; and (B) the law of the State provides that such a permit is to be issued only after an authorized government official has verified that the information available to such official does not indicate that possession of ammunition by such other person would be in violation of law. (3) Paragraphs (2) and (4) through (7) of subsection (s) shall apply with respect to ammunition transfers pursuant to this subsection in the same manner in which such paragraphs apply with respect to firearm transfers. (4) It shall be unlawful for a licensed importer, licensed manufacturer, or licensed dealer to transfer possession of ammunition to another person not so licensed unless\u2014 (A) the licensee has provided such other person with a notice of the prohibition under paragraph (1); and (B) such other person has certified that such other person has been provided with the notice described in subparagraph (A) on a form prescribed by the Attorney General. .\n##### (b) Technical and conforming amendments\n**(1) Section 922**\nSection 922(y)(2) of title 18, United States Code, is amended, in the matter preceding subparagraph (A), by striking , (g)(5)(B), and (s)(3)(B)(v)(II) and inserting and (g)(5)(B) .\n**(2) Section 925A**\nSection 925A of title 18, United States Code, is amended by striking subsection (s) or (t) of section 922 and inserting section 922(s) .\n**(3) Section 925B**\nSection 925B of title 18, United States Code, is amended by striking section 922(t) each place it appears and inserting section 922(s) .\n**(4) Brady Handgun Violence Prevention Act**\nSection 103(l) of the Brady Handgun Violence Prevention Act ( 34 U.S.C. 40901(l) ) is amended, in the matter preceding paragraph (1), by striking (t) and inserting (s) .\n**(5) Consolidated and further continuing appropriations act, 2012**\nSection 511 of title V of division B of the Consolidated and Further Continuing Appropriations Act, 2012 ( 34 U.S.C. 40901 note; Public Law 112\u201355 ) is amended by striking subsection 922(t) each place it appears and inserting subsection (s) or (t) of section 922 .\n**(6) NICS Improvement Amendments Act of 2007**\nSection 103(f) of the NICS Improvement Amendments Act of 2007 ( 34 U.S.C. 40913(f) ) is amended by striking 922(t) and inserting 922(s) .\n##### (c) Rules of construction\nNothing in this section, or any amendment made by this section, shall be construed to\u2014\n**(1)**\nauthorize the establishment, directly or indirectly, of a national firearms or ammunition registry; or\n**(2)**\ninterfere with the authority of a State, under section 927 of title 18, United States Code, to enact a law on the same subject matter as this section.\n##### (d) Authorization of increased funding for the NICS system\nIn addition to any amount otherwise authorized to be appropriated for the national instant criminal background check system established under section 103 of the Brady Handgun Violence Prevention Act ( 34 U.S.C. 40901 ), there are authorized to be appropriated not more than $150,000,000 for upgrading and maintaining the system.\n#### 7. Reporting requirement\nNot later than 180 days after the effective date under section 8 and annually thereafter, the Director of the Bureau of Alcohol, Tobacco, Firearms, and Explosives shall prepare, publish in the Federal Register, and otherwise make available to the public a report on the violations of subsection (aa) of section 922 of title 18, United States Code, as added by section 5, that occurred during the period covered by the report, and the information reported pursuant to paragraph (2)(C) of such subsection (including geographic data, total sales data, crime statistics, information on repeat offenders, or caliber types involved) during the period covered by the report, which shall include an identification of any trend in the violations or information that Federal, State, or local law enforcement agencies may find useful.\n#### 8. Effective date\nThe amendments made by this Act shall take effect on the date that is 120 days after the date of enactment of this Act.",
      "versionDate": "2025-06-26",
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
        "actionDate": "2025-06-27",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "4227",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "AMMO Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-07-25T12:15:08Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2191is.xml"
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
      "title": "AMMO Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-09T11:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "AMMO Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T03:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ammunition Modernization and Monitoring Oversight Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T03:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to prevent bulk sales of ammunition, promote recordkeeping and reporting about ammunition, end ammunition straw purchasing, and require a background check before the transfer of ammunition by certain Federal firearms licensees to non-licensees.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-16T03:33:22Z"
    }
  ]
}
```
