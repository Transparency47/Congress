# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3614?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3614
- Title: FIRE Act
- Congress: 119
- Bill type: HR
- Bill number: 3614
- Origin chamber: House
- Introduced date: 2025-05-26
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-26: Introduced in House
- 2025-05-26 - IntroReferral: Introduced in House
- 2025-05-26 - IntroReferral: Introduced in House
- 2025-05-26 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-26 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-26: Introduced in House

## Actions

- 2025-05-26 - IntroReferral: Introduced in House
- 2025-05-26 - IntroReferral: Introduced in House
- 2025-05-26 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-26 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-26",
    "latestAction": {
      "actionDate": "2025-05-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3614",
    "number": "3614",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "K000400",
        "district": "37",
        "firstName": "Sydney",
        "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
        "lastName": "Kamlager-Dove",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "FIRE Act",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-26",
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
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-26",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-26",
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
          "date": "2025-05-26T13:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-26T13:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-05-26",
      "state": "DC"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-05-26",
      "state": "NJ"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-05-26",
      "sponsorshipWithdrawnDate": "2025-06-03",
      "state": "AL"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-05-26",
      "sponsorshipWithdrawnDate": "2025-06-03",
      "state": "FL"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-05-26",
      "sponsorshipWithdrawnDate": "2025-06-03",
      "state": "MD"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "CA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "CA"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "False",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "CA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "LA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "MI"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3614ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3614\nIN THE HOUSE OF REPRESENTATIVES\nMay 26, 2025 Ms. Kamlager-Dove (for herself, Mr. Moore of Alabama , Mr. Rutherford , Mr. Ivey , Ms. Norton , and Mrs. McIver ) introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish fair labor standards, occupational safety protections, and post-incarceration career opportunities for incarcerated individuals engaged in firefighting and to provide previously incarcerated firefighters an opportunity to expunge records of disposition after successful completion of court-imposed probation, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Fairness, Inclusion, Rehabilitation, and Expungement for Incarcerated Firefighters Act or the FIRE Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1.\u2002Short title; table of contents.\nSec.\u20022.\u2002Coverage of incarcerated firefighters under the Occupational Safety and Health Act of 1970.\nSec. 3.\u2002Coverage of incarcerated firefighters under the Fair Labor Standards Act of 1938.\nSec. 4.\u2002Incentives for States to enact protections for incarcerated firefighters.\nSec. 5.\u2002Grants to assist States in covering incarcerated firefighters.\nSec.\u20026.\u2002Incarcerated firefighter reentry program grants.\nSec. 7.\u2002Expungement of certain offenses.\n#### 2. Coverage of incarcerated firefighters under the occupational safety and health act of 1970\n##### (a) Definition of correctional facility\nSection 3 of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 652 ) is amended by adding at the end the following:\n(15) The term correctional facility has the meaning given the term in section 3(aa) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 )(aa). .\n##### (b) State plans\nSection 18 of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 667 ) is amended\u2014\n**(1)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (6), by inserting, including incarcerated firefighters as defined in section 3(z) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 )(z), after political subdivisions, ; and\n**(B)**\nin paragraph (7)\u2014\n**(i)**\nby striking (7) requires and inserting (7)(A) requires ; and\n**(ii)**\nby adding at the end the following:\n(B) requires the State to ensure that any public agency of the State (or of a political subdivision of the State) operating a correctional facility or contracting with a private entity to operate such a facility, shall, not later than 2 years after the date of enactment of the FIRE Act, and every year thereafter, submit to the Attorney General and Congress a report on\u2014 (i) the workplace safety and health conditions at each such facility, and (ii) any potential noncompliance of each such facility with the safety and health standards under the State plan, and .\n##### (c) Federal prisons\nSection 19 of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 668 ) is amended by adding at the end the following:\n(e) Bureau of prisons (1) In general The Director of the Bureau of Prisons shall\u2014 (A) ensure that the occupational safety and health program established and maintained by the Director under subsection (a) applies with respect to incarcerated firefighters in the same manner as the program applies to employees of the Bureau of Prisons; and (B) submit, not later than 2 years after the date of enactment of the FIRE Act, and every year thereafter, to the Attorney General and Congress, a report on\u2014 (i) the workplace safety and health conditions at any correctional facility operated by the Bureau of Prisons or a private entity contracting with the Bureau of Prisons; (ii) any injury or death of any employee or incarcerated firefighter while performing labor with respect to such facility; and (iii) any potential noncompliance of any such facility of such occupational safety and health program. (2) Incarcerated firefighter In this section, the term incarcerated firefighter means an individual who is incarcerated in a correctional facility operated by the Bureau of Prisons or facilitated or operated by a private entity through a contract with the Bureau of Prisons and who performs firefighting or emergency response services work offered or required by or through the correctional facility, including work associated with prison work programs, work release programs, public works programs, restitution centers, correctional facility operations and maintenance, or private entities. .\n#### 3. Coverage of incarcerated firefighters under the fair labor standards act of 1938\nSection 3 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 ) is amended\u2014\n**(1)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (B), by striking ; and and inserting a semicolon;\n**(ii)**\nin subparagraph (C)(ii)(V), by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(D) any individual employed as an incarcerated firefighter by a public agency that operates the correctional facility in which such individual is incarcerated or detained. ; and\n**(B)**\nby adding at the end the following:\n(6) The term employee includes any individual employed as an incarcerated firefighter by a private entity that operates, through a contract with a public agency, the correctional facility in which such individual is incarcerated or detained. ;\n**(2)**\nin subsection (m)(1), by striking any employee. and inserting any employee: Provided further, That, in the case of an employee who is an incarcerated firefighter, the cost of board, lodging, or other facilities and any amount taken from amounts paid such incarcerated firefighter for payment of a court-imposed fee shall not be included in the wage paid to such employee. ; and\n**(3)**\nby adding at the end the following:\n(z) (1) The term incarcerated firefighter means an individual who is incarcerated in a correctional facility operated by a public agency or facilitated or operated by a private entity through a contract with a public agency and who performs firefighting or emergency response services work offered or required by or through the correctional facility, including work associated with prison work programs, work release programs, State prison industries, public works programs, restitution centers, correctional facility operations and maintenance, or private entities. (2) An incarcerated firefighter shall be considered employed by\u2014 (A) the public agency operating the correctional facility in which the individual is incarcerated or detained; or (B) in a case in which the individual is incarcerated or detained in a correctional facility operated by a private entity through a contract with a public agency, such private entity. (aa) Correctional facility means a jail, prison, or other detention facility used to house people who have been arrested, detained, held, or convicted by a criminal justice agency or a court. (bb) (1) Court-imposed fee means any fee imposed by a court as a result of a criminal conviction, including any surcharge imposed for a felony or misdemeanor conviction, a criminal justice administrative fee, a court-appointed attorney fee, a court clerk fee, a filing clerk fee, a DNA database fee, a jury fee, a crime lab analysis fee, a late fee, an installment fee, or any other court cost. (2) The term court-imposed fee does not include any amount required by a court to be paid for child support, to a crime victim compensation fund, for a civil judgment, or for a criminal fine. .\n#### 4. Incentives for states to enact protections for incarcerated firefighters\nTitle I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10101 et seq. ) is amended\u2014\n**(1)**\nin section 501 ( 34 U.S.C. 10152 ), by adding at the end the following:\n(i) Annual report on workplace safety and health conditions Not later than 2 years after the date of enactment of the FIRE Act, and annually thereafter, any State or unit of local government that receives a grant under this section and operates a correctional facility or contracts with a private entity to operate a correctional facility shall submit to the Attorney General and Congress a report on\u2014 (2) the workplace safety and health conditions at each such correctional facility; (3) any injury or death of any\u2014 (A) employee; or (B) incarcerated firefighter while such firefighter was performing work required to be performed during their incarceration; and (4) any potential noncompliance of any such correctional facility with the occupational safety and health standards that apply to the correctional facility. ;\n**(2)**\nin section 502(a) ( 34 U.S.C. 10153(a) ), by adding at the end the following:\n(7) As applicable, a certification that,\u2014 (A) the State or unit of local government has provided workplace safety and health protections for incarcerated firefighters in correctional facilities, either by legislative or executive action, that are at least as effective in providing safe and healthful employment and places of employment for incarcerated firefighters as the comprehensive occupational safety and health programs established by States under section 18 of the Occupational Safety and Health Act of 1970; or (B) an appropriate State or local agency monitors and enforces or will monitor or enforce, as applicable, the safety and health protections described in subparagraph (A). ;\n**(3)**\nin section 506 ( 34 U.S.C. 10157 ), by adding at the end the following:\n(c) Of the total amount made available to carry out this subpart for a fiscal year, the Attorney General, in consultation with the Assistant Secretary of Labor for Occupational Safety and Health, shall reserve $400,000 for use by States and units of local government to establish and implement workplace safety and health protections for incarcerated firefighters. ; and\n**(4)**\nin section 901(a) ( 34 U.S.C. 10251(a) )\u2014\n**(A)**\nin paragraph (32), by striking and at the end;\n**(B)**\nin paragraph (33), by striking the period at the end and adding ; and ; and\n**(C)**\nby inserting after paragraph (33) the following:\n(34) the term incarcerated firefighter shall have the meaning given such term in section 3(z) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(z) ). .\n#### 5. Grants to assist states in covering incarcerated firefighters\n##### (a) In general\nThe Secretary of Labor shall establish a grant program to award a grant to each State that submits an application satisfying the requirements under subsection (b) to assist the State in amending the occupational safety and health laws of the State to cover incarcerated firefighters and to enforce those laws as appropriate through inspections, investigations, citations, penalties, and other enforcement mechanisms.\n##### (b) Applications\nA State seeking a grant under this section shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may reasonably require.\n##### (c) Definition of incarcerated firefighter\nIn this section, the term incarcerated fighter has the meaning given such term in section 18(i) (as amended by section 2(b)(2) of this Act) of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 667(i) ).\n##### (d) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $100,000,000 for each of fiscal years 2026 through 2031, to remain available until expended.\n#### 6. Incarcerated firefighter reentry program grants\n##### (a) In general\nSubtitle D of title I of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3221 et seq. ) is amended\u2014\n**(1)**\nby redesignating section 172 as section 173; and\n**(2)**\nby inserting after section 171 the following new section:\n172. Incarcerated firefighter reentry program grants (a) In general The Secretary shall establish a program to award grants to eligible entities to enable such entities to provide job training, job placement services, and mentoring to individuals who are former incarcerated firefighters during reentry. (b) Application To be eligible for a grant under this section, a State shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may reasonably require. (c) Use of funds A grant awarded under this section may be used by an eligible entity to\u2014 (1) in the case of a program that provides job training, placement services, and mentoring exclusively to former incarcerated firefighters upon reentry, to pay costs related to such program; and (2) in the case of a program that provides job training, placement services, and mentoring to former incarcerated firefighters and to other individuals during reentry, to pay costs related to the participation of such former incarcerated firefighters in the program. (3) evaluate and implement methods to improve the employment opportunities of incarcerated firefighters upon reentry; and (4) identify, and make recommendations regarding, best practices relating to reentry and the employment of incarcerated firefighters as full-time firefighters during reentry. (d) Definitions In this section: (1) Eligible entity The term eligible entity means\u2014 (A) a private non-profit organization under section 501(c)(3) of the Internal Revenue Code of 1986; (B) a local workforce development board; (C) a State or local government; or (D) an Indian or Native American entity eligible for grants under section 166. (2) Incarcerated firefighter The term incarcerated firefighter has the meaning given such term in section 3(z) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(z) ). (3) Reentry period The term reentry means, in relation to an individual, the 180-day period beginning on the date on which such individual is released from incarceration. .\n##### (b) Authorization of appropriations\nSection 173(d) of the Workforce Innovation and Opportunity Act as redesignated by subsection (a) of this section is amended by striking section 169 and inserting sections 169 and 172 .\n##### (c) Clerical amendment\nThe table of contents in section 1(b) of the Workforce Innovation and Opportunity Act is amended\u2014\n**(1)**\nby redesignating the item relating to section 172 as section 173; and\n**(2)**\nby inserting after the item relating to section 171 the following:\n173. Incarcerated firefighter reentry program grants .\n#### 7. Expungement of certain offenses\n##### (a) In general\nAn eligible incarcerated firefighter may file a petition under this section for expungement.\n##### (b) Extenuating circumstances\nIf extenuating circumstances prevent an incarcerated firefighter from fulfilling the requirements of their sentence, as required under subsection (i)(1), the court, in its discretion, may waive a portion of such requirement and determine the incarcerated firefighter is an eligible incarcerated firefighter.\n##### (c) Procedure for expungement\n**(1) Petition**\nA petition for expungement may be filed only in the court in which the eligible incarcerated firefighter was convicted of the offense for which expungement is sought. The clerk of the court shall serve that petition on the United States attorney for that district. Except as provided under paragraph (5), not later than 60 days after service of such petition, the United States attorney may submit recommendations to the court and provide a copy of those recommendations to the firefighter.\n**(2) Appointment of counsel**\nThe court shall appoint counsel upon the request of an indigent eligible incarcerated firefighter to represent the firefighter in proceedings under this section, including the preparation of a petition or subsequent petition under this section.\n**(3) Submission of evidence**\nThe eligible incarcerated firefighter and the U.S. attorney, as noted under paragraph (1), may file with the court evidence relating to the petition.\n**(4) Basis for decision**\nIn making a decision on the petition, the court shall consider all evidence and weigh the interests of the eligible incarcerated firefighter, the best interests of justice, and public safety.\n**(5) Subsequent petition**\nIf the court denies the petition, the petitioner may not file another such petition under paragraph (1) until the date that is 2 years after the date of such denial.\n**(6) Mandatory grant of petition**\nExcept as provided in subparagraph (B), the court shall grant the petition of an eligible incarcerated firefighter who files the petition on a date that is not earlier than the date that is 7 years after the date on which the petitioner has fulfilled the requirements of the sentence, as described in subsection (i)(1). The United States Attorney may not submit recommendations under paragraph (1) with regard to that petition.\n**(7) Discretionary grant of petition**\nExcept as provided in subparagraph (B), the court may grant the petition of an eligible incarcerated firefighter who files the petition on a date that is not earlier than the date that is 1 year after the date on which the petitioner has fulfilled the requirements of the sentence, as described in subsection (i)(1).\n##### (d) Notification of expungement\nNot later than 7 days after granting an expungement petition, in order to facilitate the timely update of relevant records, the court shall send a copy of the petition and final order to\u2014\n**(1)**\nthe Attorney General of the United States;\n**(2)**\nthe chief law enforcement officer of the State in which the crime was committed;\n**(3)**\nthe chief law enforcement officer of the State in which the eligible incarcerated firefighter resides;\n**(4)**\nany local law enforcement agency that serves the jurisdiction in which the crime was committed; and\n**(5)**\nany local law enforcement agency that serves the jurisdiction in which the eligible incarcerated firefighter resides.\n##### (e) Effect of expungement\n**(1) In general**\nAn order granting expungement under this section shall restore the eligible incarcerated firefighter concerned, in the contemplation of the law, to the status such individual occupied before the arrest or institution of criminal proceedings for the offense that was the subject of the expungement.\n**(2) Sentencing**\nIn determining an appropriate sentence for unrelated subsequent criminal conduct, a court of the United States shall not consider an expunged criminal conviction for the purposes of determining the appropriate sentencing range pursuant to the United States Sentencing Guidelines, or to sentence a person outside of that sentencing range.\n**(3) No disqualification; statements**\nAn eligible incarcerated firefighter whose petition under this section is granted shall not be required to divulge information pertaining to the offense with regard to which expungement was granted, nor shall such firefighter be held under any provision of law guilty of perjury, false answering, or making a false statement by reason of the failure of the firefighter to recite or acknowledge such arrest or institution of criminal proceedings, or results thereof, in response to an inquiry made of the firefighter for any purpose. The fact that such firefigher has been convicted of the offense concerned shall not operate as a disqualification of such individual to pursue or engage in any lawful activity, occupation, or profession.\n**(4) Records expunged**\nExcept as provided under subsection (f), on the grant of a petition under this section, the following shall be expunged:\n**(A)**\nAny official record relating to the arrest of the eligible incarcerated firefighter, the institution of criminal proceedings against the firefighter, or the results thereof including conviction for the offense with regard to which expungement is sought.\n**(B)**\nAny reference in any official record to the arrest of the eligible incarcerated firefighter, the institution of criminal proceedings against the firefighter, or the results thereof including conviction for the offense with regard to which expungement is sought.\n**(5) Exceptions**\nThe Attorney General may make rules providing for exceptions to paragraph (4) as the Attorney General determines necessary to serve the interests of justice and public safety.\n##### (f) Disclosure of expunged records\n**(1) Department of justice records**\nThe Attorney General shall retain an unaltered nonpublic copy of\u2014\n**(A)**\nany record that is expunged; and\n**(B)**\nany record containing a reference that is expunged.\n**(2) Law enforcement purposes**\nThe Attorney General shall maintain a nonpublic index of the records described under paragraph (1) containing, for each such record, only the name of, and alphanumeric identifiers that relate to, the eligible incarcerated firefighter who is the subject of such record, the word expunged , and the name of the person, agency, office, or department that has custody of the expunged record, and shall not name the offense committed. The index shall be made available only to an entity to which records may be made available under paragraph (4) or to any Federal or State law enforcement agency that has custody of such records.\n**(3) Court records**\nThe court shall retain an unaltered nonpublic copy of\u2014\n**(A)**\nany record that is expunged; and\n**(B)**\nany record containing a reference that is expunged.\n**(4) Authorized disclosures**\n**(A) In general**\nExcept as provided in subparagraph (B), any record described in paragraph (1) pertaining to an individual may be made available only\u2014\n**(i)**\nto the eligible incarcerated firefighter;\n**(ii)**\nto a Federal or State court or Federal, State, or local law enforcement agency, in the case of a criminal investigation or prosecution of an individual or in conducting a background check on an individual who has applied for employment by such court or agency; or\n**(iii)**\nto a Federal or State court or Federal, State, or local law enforcement agency for the exclusive purpose of maintaining accurate official records.\n**(B) Authorized disclosure to individuals**\nOn application of the eligible incarcerated firefighter, the record may be available to an individual identified in the firefighter\u2019s application.\n##### (g) Punishment for improper disclosure\nWhoever intentionally makes or attempts to make a disclosure, other than a disclosure authorized under subsection (f), of any record or reference that is expunged under this section, shall be fined under title 18, United States Code, imprisoned not more than one year, or both.\n##### (h) Effective date\nThe amendments made by this section shall apply to individuals convicted of an offense before, on, or after the date of the enactment of this Act.\n##### (i) Definitions\nIn this section\u2014\n**(1) Eligible incarcerated firefighter**\nThe term eligible incarcerated firefighter means an incarcerated firefighter convicted of an offense who has fulfilled the requirements of the sentence of the court in which the firefighter was convicted, including\u2014\n**(A)**\npaying, or consistently fulfilling obligations of a payment plan for, all applicable fines, restitutions, or assessments;\n**(B)**\ncompletion of any term of imprisonment or period of probation;\n**(C)**\nmeeting all conditions of supervised release; and\n**(D)**\nif so required by the terms of the sentence, remaining free from dependency on or abuse of alcohol or a controlled substance for a period of not less than 1 year.\n**(2) Incarcerated firefighter**\nThe term incarcerated firefighter shall have the meaning given such term in section 3(z) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(z) ).",
      "versionDate": "2025-05-26",
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
        "updateDate": "2025-06-25T10:51:30Z"
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
      "date": "2025-05-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3614ih.xml"
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
      "title": "FIRE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-13T03:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FIRE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-13T03:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fairness, Inclusion, Rehabilitation, and Expungement for Incarcerated Firefighters Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-13T03:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish fair labor standards, occupational safety protections, and post-incarceration career opportunities for incarcerated individuals engaged in firefighting and to provide previously incarcerated firefighters an opportunity to expunge records of disposition after successful completion of court-imposed probation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-13T03:33:15Z"
    }
  ]
}
```
